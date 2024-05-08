import unittest
from python_assignment.src.named_tuple.util import calculate_average_mark


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = calculate_average_mark()
        expected_output = 84.75
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
