import unittest
from python_assignment.src.min_max.util import max_of_min_in_rows


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = max_of_min_in_rows()
        expected_output = 2
        self.assertEqual(actual_output, expected_output)

    def test_case1(self):
        actual_output = max_of_min_in_rows()
        expected_output = 0
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
