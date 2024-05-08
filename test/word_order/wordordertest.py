import unittest
from python_assignment.src.word_order.util import word_order


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_input = word_order(4, ['aac', 'bbad', 'bcde', 'aace'])
        expected_output = (4, [1, 1, 1, 1])
        self.assertEqual(actual_input, expected_output)  # add assertion here

    def test_case1(self):
        actual_input = word_order(5, ['apple', 'banana', 'apple', 'orange', 'banana'])
        expected_output = (3, [2, 2, 1])
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()
