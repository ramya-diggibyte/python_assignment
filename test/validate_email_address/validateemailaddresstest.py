import unittest
from python_assignment.src.validate_email_address.util import validate_email_address


class MyTestCase(unittest.TestCase):
    def test_case(self):
        valid_email = "janetramya04@example.com"
        self.assertTrue(validate_email_address(valid_email))

    def test_case1(self):
        valid_email = "jim@gmail.com"
        self.assertTrue(validate_email_address(valid_email))

if __name__ == '__main__':
    unittest.main()