import unittest
from python_assignment.src.floor_ceil.util import floor_ceil_rint


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = floor_ceil_rint([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
        expected_output = "[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]\n[  2.   3.   4.   5.   6.   7.   8.   9.  10.]\n[  1.   2.   3.   4.   6.   7.   8.   9.  10.]"
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        actual_output = floor_ceil_rint([2.1, 2.2, 3.1, 3.3, 5.5, 6.6, 7.7, 3.8, 4.9])
        expected_output = "[ 2.  2.  3.  3.  5.  6.  7.  3.  4.]\n[ 3.  3.  4.  4.  6.  7.  8.  4.  5.]\n[ 2.  2.  3.  3.  6.  7.  8.  4.  5.]"
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()