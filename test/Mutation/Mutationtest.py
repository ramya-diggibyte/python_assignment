import unittest
from python_assignment.src.Mutation.util import mutate_string

class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_input = mutate_string("lliteral", 0, "")
        expected_output ="literal"
        self.assertEqual(actual_input, expected_output)  # add assertion here
    def test_case1(self):
        actual_input = mutate_string("organizer", 8, "")
        expected_output = "organize"
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()


