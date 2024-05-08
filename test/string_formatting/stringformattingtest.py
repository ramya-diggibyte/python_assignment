import unittest
from python_assignment.src.string_formatting.util import print_formatted


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = print_formatted(4)
        expected_output = "1   1   1   1\n2   2   2  10\n3   3   3  11\n4   4   4 100"
        self.assertEqual(actual_output, expected_output)
    def test_case1(self):
        actual_output = print_formatted(2)
        expected_output = "1  1  1  1\n2  2  2 10"
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
