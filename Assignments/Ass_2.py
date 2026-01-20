# String Assignment. (This can be tricky so feel free to watch solution so we can do it together)
#
# - Ask the user how many days until their birthday
#
# - Using the print()function. Print an approx. number of weeks until their birthday
#
# - 1 week is = to 7 days.


days = int(input("How many days before your B'day??"))
number_of_weeks = days // 7
number_of_days = days % 7

print(f"Hi Your B'day is away from "
      f"{number_of_weeks} weeks and "
      f"{number_of_days} days")

