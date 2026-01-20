# Write a Python program that can do the following:
#
# - You have $50
#
# - You buy an item that is $15, that has a 3% tax
#
# - Using the print()  Print how much money you have left, after purchasing the item.

current_amount = 50
bought_item = 15
tax = 0.03

remaining_money = current_amount - (bought_item + (bought_item * tax))
print(remaining_money)