#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorageTest(unittest.TestCase):
    """
    Test case of the FileStorage class
    """

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
