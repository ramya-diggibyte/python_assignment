import unittest
from python_assignment.src.linear_algebra.util import linear_algebra


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = linear_algebra([[-7.1, 1.7], [8.1, 1.8]])
        expected_output = -26.6
        self.assertEqual(actual_output, expected_output)  # add assertion here

    def test_case1(self):
        actual_output = linear_algebra([[3, 2], [2, 3]])
        expected_output = 5.0
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
