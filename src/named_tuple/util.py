from collections import namedtuple

def calculate_average_mark():
    N = int(input("Enter the number of students: "))
    student_fields = input("Enter the fields for student namedtuple separated by space: ").split()
    student = namedtuple('student', student_fields)
    marks_sum = sum(float(input(f"Enter marks for {student_fields[-1]} of student {i + 1}: ").split()[-1]) for i in range(N))
    average_mark = marks_sum / N
    return average_mark