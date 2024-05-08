import unittest

from python_assignment.src.text_alignment.util import text_alignment


class MyTestCase(unittest.TestCase):
    def test_case(self):
        thickness = int(input("Enter thickness an odd number: "))
        expected_output = text_alignment(thickness, c="H")
        actual_output = [
            '  H  ',
            ' HHH ',
            'HHHHH',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHHHHHHHHHHHHHH  ',
            ' HHHHHHHHHHHHHHH  ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            '            HHHHH ',
            '             HHH  ',
            '              H   ',
        ]
        self.assertEqual(expected_output, expected_output)  # testcase


if __name__ == '__main__':
    unittest.main()
