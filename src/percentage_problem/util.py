def percent_calculation(student_marks, name):
    n = len(student_marks[name])  # student_marks:dictionary, name:key
    print(n)
    total_marks = sum(student_marks[name])
    print(total_marks)
    avg = format(total_marks / n, '.2f')
    return avg
