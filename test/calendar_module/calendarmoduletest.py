import unittest
from python_assignment.src.calendar_module.util import day_of_week


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = day_of_week("07 04 1992")
        expected_output = "SATURDAY"
        self.assertEqual(actual_output, expected_output)  # add assertion here

    def test_case1(self):
        actual_output = day_of_week("05 01 2019")
        expected_output = "WEDNESDAY"
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
