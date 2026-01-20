def calculate_homework(homework_assignment_grades):
    sum_of_grades = 0
    for key, value in homework_assignment_grades.items():
        sum_of_grades += value
    final_grade = round(sum_of_grades / len(homework_assignment_grades),2)
    print(homework_assignment_grades)
    print(final_grade)

