import unittest
from python_assignment.src.iterables_iterators.util import iterables_iterators


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = iterables_iterators(4, "aacd", 2)
        expected_output = 0.8333333
        self.assertEqual(actual_output, expected_output)

    def test_case1(self):
        actual_output = iterables_iterators(5, "abcdff", 2)
        expected_output = 0.3333333
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
