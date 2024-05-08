import unittest
from python_assignment.src.second_max_number.util import second_max_number


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_input = second_max_number([10,12,17])
        expected_output = 12
        self.assertEqual(actual_input, expected_output)

    def test_case2(self):
        actual_input = second_max_number([2, 7, 7, 9, 3])
        expected_output = 7
        self.assertEqual(actual_input, expected_output)




if __name__ == '__main__':
    unittest.main()
