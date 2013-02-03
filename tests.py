# -*- coding: utf-8 -*-
import os
import sys
import unittest

from mega import Mega


class TestMega(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        email = os.environ.get('MEGAEMAIL') or sys.argv[0]
        password = os.environ.get('MEGAPASSWORD') or sys.argv[1]
        self.api_logged = Mega.from_credentials(email, password)
        self.api_ephemeral = Mega.from_ephemeral()

    def _check_file_exists(self, file_name, files):
        uploaded = False
        for f in files['f']:
            if isinstance(f['a'], dict):
                if f['a'].get('n') == file_name:
                    uploaded = True
        return uploaded

    def _test_upload_file(self, api):
        api.get_files()
        api.uploadfile('tests.py')  # inception
        files = api.get_files()
        uploaded = self._check_file_exists('tests.py', files)
        self.assertEqual(uploaded, True)

    def test_upload_file_logged(self):
        self._test_upload_file(self.api_logged)

    def test_upload_file_ephemeral(self):
        self._test_upload_file(self.api_ephemeral)

if __name__ == '__main__':
    unittest.main()
