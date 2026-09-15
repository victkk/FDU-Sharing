import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('agent', Path(__file__).with_name('maintainer.py'))
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)


class AgentTests(unittest.TestCase):
    def test_protected_policy_and_path_traversal(self):
        for p in ['.github/agent/maintainer.py', '.github/workflows/run.yml',
                  'x/AGENTS.md', '.github/CODEOWNERS', '../escape', '/tmp/file', '-option']:
            with self.subTest(p=p), self.assertRaises(ValueError):
                a.validate_paths([p])
        a.validate_paths(['.github/CONTRIBUTING.md', 'pages/courses/_meta.ts'])

    def test_comment_dedup_does_not_trust_forged_marker(self):
        fake = {'user': {'login': 'contributor'}, 'body': '<!-- marker -->'}
        with patch.object(a, 'pages', return_value=[fake]), patch.object(a, 'api') as api:
            a.bot_comment(23, '<!-- marker -->', 'review')
            api.assert_called_once()
        fake['user']['login'] = 'github-actions[bot]'
        with patch.object(a, 'pages', return_value=[fake]), patch.object(a, 'api') as api:
            a.bot_comment(23, '<!-- marker -->', 'review')
            api.assert_not_called()

    def test_changed_source_never_merges(self):
        meta = {'number': 23, 'head': 'oldhead', 'base': 'base', 'base_ref': 'master'}
        import json
        with patch.dict(os.environ, {'CANDIDATE_META': json.dumps(meta), 'BUILD_RESULT': 'success'}), \
             patch.object(a, 'api', side_effect=[{'state': 'open', 'draft': False,
                'head': {'sha': 'newhead'}}, {'object': {'sha': 'base'}}]), \
             patch.object(a, 'git') as git:
            a.finish()
            git.assert_not_called()

    def test_failed_build_never_merges(self):
        import json
        meta = {'number': 23, 'marker': 'marker', 'summary': 'review'}
        with patch.dict(os.environ, {'CANDIDATE_META': json.dumps(meta), 'BUILD_RESULT': 'failure', 'RUN_URL': 'url'}), \
             patch.object(a, 'bot_comment') as comment, patch.object(a, 'git') as git:
            a.finish()
            git.assert_not_called()
            comment.assert_called_once()

    def test_conflict_resolution_and_review_in_real_git(self):
        old = os.getcwd()
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            try:
                a.git('init', '-b', 'master')
                a.git('config', 'user.name', 'test')
                a.git('config', 'user.email', a.EMAIL)
                a.git('config', 'core.quotePath', 'false')
                Path('pages/courses').mkdir(parents=True)
                for name in ('old', 'base', 'head'):
                    Path('pages/courses/' + name + '.mdx').write_text('# Course')
                file = Path('pages/courses/_meta.ts')
                file.write_text("export default {\n  'old': 'old',\n}\n")
                a.git('add', '.'); a.git('commit', '-m', 'ancestor')
                ancestor = a.git('rev-parse', 'HEAD').strip()
                file.write_text("export default {\n  'old': 'old',\n  'base': 'base',\n}\n")
                a.git('add', '.'); a.git('commit', '-m', 'base')
                base = a.git('rev-parse', 'HEAD').strip()
                a.git('checkout', '-b', 'contributor', ancestor)
                file.write_text("export default {\n  'old': 'old',\n  'head': 'head',\n}\n")
                a.git('add', '.'); a.git('commit', '-m', 'head')
                head = a.git('rev-parse', 'HEAD').strip()
                Path('remote.git').mkdir()
                a.run('git', 'init', '--bare', 'remote.git')
                a.git('remote', 'add', 'origin', str(Path('remote.git').absolute()))
                a.git('push', 'origin', 'master', 'contributor')
                merged = "export default {\n  'old': 'old',\n  'base': 'base',\n  'head': 'head',\n}\n"
                pr = {'number': 23, 'draft': False, 'state': 'open', 'title': 'test',
                      'base': {'sha': base, 'ref': 'master'}, 'head': {'sha': head, 'ref': 'contributor'}}
                answers = [{'resolved': True, 'files': [{'path': str(file), 'content': merged}]},
                           {'approve': True, 'summary': 'reviewed'}]
                with patch.object(a, 'api', side_effect=lambda path: {'default_branch': 'master'} if not path else {'object': {'sha': base}}), \
                     patch.object(a, 'model', side_effect=answers), patch.object(a, 'outputs') as out:
                    a.prepare_pr(pr)
                meta = out.call_args.kwargs['meta']
                self.assertEqual(a.show(meta['commit'], str(file)), merged)
                self.assertEqual(a.git('show', '-s', '--format=%P', meta['commit']).strip(), base + ' ' + head)
                self.assertEqual(a.git('show', '-s', '--format=%ae', meta['commit']).strip(), a.EMAIL)
            finally:
                os.chdir(old)


if __name__ == '__main__':
    unittest.main()
