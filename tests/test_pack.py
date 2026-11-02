import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from install import install
from validate import SECTIONS, validate


class PackTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name).resolve()
        self.source = self.base / 'source'
        self.project = self.base / 'project'
        self.project.mkdir()
        self.skill = self.source / 'skills' / 'example-skill' / 'SKILL.md'
        self.skill.parent.mkdir(parents=True)
        self.text = '---\nname: example-skill\ndescription: "Use for a test fixture."\n---\n' + ''.join(f'## {s}\nTest.\n' for s in SECTIONS)
        self.skill.write_text(self.text)

    def test_valid_fixture(self):
        self.assertTrue(validate(self.source)['ok'])

    def test_repository(self):
        result = validate(Path(__file__).resolve().parents[1])
        self.assertTrue(result['ok'], result)

    def test_bad_frontmatter(self):
        self.skill.write_text(self.text.replace('name: example-skill', 'name: INVALID'))
        self.assertFalse(validate(self.source)['ok'])

    def test_mismatched_name(self):
        self.skill.write_text(self.text.replace('name: example-skill', 'name: wrong-name'))
        self.assertFalse(validate(self.source)['ok'])

    def test_missing_section(self):
        self.skill.write_text(self.text.replace('## Avoid\n', '## Other\n'))
        self.assertFalse(validate(self.source)['ok'])

    def test_private_path_rejected(self):
        self.skill.write_text(self.text + '\n' + '/' + 'Users' + '/fixture/private\n')
        self.assertFalse(validate(self.source)['ok'])

    def test_missing_link_rejected(self):
        self.skill.write_text(self.text + '\n[missing](references/absent.md)\n')
        self.assertFalse(validate(self.source)['ok'])

    def test_archive_dependency_rejected(self):
        self.skill.write_text(self.text + '\nRead .archive/missing\n')
        self.assertFalse(validate(self.source)['ok'])

    def test_dry_run_no_writes(self):
        result = install(self.source, self.project, 'codex', ['example-skill'])
        self.assertFalse(result['applied'])
        self.assertEqual(list(self.project.iterdir()), [])

    def test_install_both_targets_and_content(self):
        for target, folder in [('codex', '.agents'), ('claude', '.claude')]:
            result = install(self.source, self.project, target, ['example-skill'], True)
            self.assertTrue(result['applied'])
            self.assertEqual((self.project / folder / 'skills/example-skill/SKILL.md').read_text(), self.text)

    def test_collision_no_overwrite(self):
        install(self.source, self.project, 'codex', ['example-skill'], True)
        dest = self.project / '.agents/skills/example-skill/SKILL.md'
        dest.write_text('pre-existing user content')
        with self.assertRaises(FileExistsError):
            install(self.source, self.project, 'codex', ['example-skill'], True)
        self.assertEqual(dest.read_text(), 'pre-existing user content')

    def test_unknown_and_traversal_names(self):
        for names in [['missing'], ['../outside'], ['example-skill', 'example-skill']]:
            with self.assertRaises(ValueError):
                install(self.source, self.project, 'codex', names, True)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_destination_symlink_rejected(self):
        other = self.base / 'other'
        other.mkdir()
        (self.project / '.agents').symlink_to(other, target_is_directory=True)
        with self.assertRaises(ValueError):
            install(self.source, self.project, 'codex', ['example-skill'], True)
        self.assertEqual(list(other.iterdir()), [])

    def test_support_file_rejected(self):
        (self.skill.parent / 'unexpected.txt').write_text('unreviewed')
        self.assertFalse(validate(self.source)['ok'])

    def test_source_symlink_rejected(self):
        self.skill.unlink()
        outside = self.base / 'outside.md'
        outside.write_text(self.text)
        self.skill.symlink_to(outside)
        self.assertFalse(validate(self.source)['ok'])

    def test_copy_failure_removes_created_skill(self):
        with patch('install.shutil.copyfile', side_effect=OSError('simulated failure')):
            with self.assertRaises(OSError):
                install(self.source, self.project, 'codex', ['example-skill'], True)
        self.assertFalse((self.project / '.agents/skills/example-skill').exists())


if __name__ == '__main__':
    unittest.main()
