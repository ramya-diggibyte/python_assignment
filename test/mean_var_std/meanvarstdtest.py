import unittest
from python_assignment.src.mean_var_std.util import mean_var_std


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = mean_var_std([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        expected_output = "[2. 5. 8.]\n[6. 6. 6.]\n2.58198889747"
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
