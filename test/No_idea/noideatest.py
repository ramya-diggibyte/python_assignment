import unittest
from python_assignment.src.No_idea.util import happiness_noidea


class MyTestCase(unittest.TestCase):
    def test_case(self):
        n, m = 5, 6
        input_array = [1, 2, 3, 4]
        A = [4, 5]
        B = [6]
        actual_output = happiness_noidea(n, m, input_array, A, B)
        expected_output = 1
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        n, m = 4, 3
        input_array = [1, 2, 3, 4]
        A = [1, 3]
        B = [2]
        actual_output = happiness_noidea(n, m, input_array, A, B)  # total happiness = 1 - 1 + 1 + 0 = 1.
        expected_output = 1
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
