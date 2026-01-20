
"""
-- Modules get used all the time throughout programing
-- IT helps for creating more files & clean and maintainability
"""

# from grade_average_service  import calculate_homework

import grade_average_service as average_service

homework_assignment_grades={
    "homework_1":85,
    "homework_2":90,
    "homework_3":100
}



average_service.calculate_homework(homework_assignment_grades)