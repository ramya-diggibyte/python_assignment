import unittest
from python_assignment.src.merge_the_tools.util import merge_the_tools


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = merge_the_tools("EMPLOYEES", 3)
        expected_output = ['EMP','LOY','ES']
        self.assertEqual(actual_output, expected_output)

    def test_case1(self):
        actual_output = merge_the_tools("CONCURRENT", 3)
        expected_output = ['CON','CUR','REN']
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
