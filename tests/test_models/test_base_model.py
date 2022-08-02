#!/usr/bin/python3
"""
BaseModel unittest
"""


# call the unittest function inside the BaseModel class
class BaseModelTest(unittest.TestCase):
    """
    Calling the test case
    """

    def test_style_check(self):
        """
        The test style that will be used is PEP8
        """
        style = pep8.StyleGuide(quiet=True)
        i = style.check_files(['models/base_model.py'])
        self.assertEqual(i.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
