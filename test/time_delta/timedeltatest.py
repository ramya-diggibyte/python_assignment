import unittest
from python_assignment.src.time_delta.util import time_difference


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = time_difference("Wed 01 May 2019 12:30:24 -0400", "Wed 01 May 2019 12:30:24 -0000")
        expected_output = 14400
        self.assertEqual(actual_output, expected_output)  # add assertion here

    def test_case1(self):
        actual_output = time_difference("Wed 08 May 2024 11:24:06 +0530", "Tue 07 May 2024 10:34:16 -0000")
        expected_output = 69590
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
