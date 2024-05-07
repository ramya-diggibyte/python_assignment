import unittest
from python_assignment.src.percentage_problem.util import *


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_input = percent_calculation({'Ramya': [20,21,23,24], 'Alanis': [7, 11, 10], 'Janet': [52,64]}, 'Alanis')
        expected_output = 9.33
        self.assertEqual(actual_input, format(expected_output, '.2f'))   # add the assertion here
        # self.assertEqual(True, False)

    def test_case2(self):
        actual_input = percent_calculation({'Alanis': [90.4,92.5,84], 'Janet': [85,64,72.4]}, 'Alanis')
        expected_output = 88.97
        self.assertEqual(actual_input, format(expected_output, '.2f'))   # add the assertion here


if __name__ == '__main__':
    unittest.main()
