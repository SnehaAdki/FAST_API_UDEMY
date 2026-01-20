# - Create a variable grade holding an integer between 0 - 100
#
# - Code if, elif, else statements to print the letter grade of the number grade variable
#
# Grades:
#
# A = 90 - 100
#
# B = 80 - 89
#
# C = 70-79
#
# D = 60 - 69
#
# F = 0 - 59
#
#
# Example:
#
# if grade = 87 then print('B')


grade = int(input("What is your grade?"))
if grade >= 90:
    print(f"{grade} A")
elif grade >= 80:
    print(f"{grade} B")
elif grade >= 70:
    print(f"{grade} C")
elif grade >= 60:
    print(f"{grade} D")
else:
    print(f"{grade} F")