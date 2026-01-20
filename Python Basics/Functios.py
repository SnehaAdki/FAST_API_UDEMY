"""
Functions
"""


# with no parameter no rtn type
def my_function():
    print("I am inside the my_function")


my_function()


# with single parameter
def print_my_name(name):
    print(f"Your Name is {name}")


print_my_name("Sneha")


# with multiple parameter
def print_my_name(f_name, l_name):
    print(f"Your Name is {f_name}  {l_name}")


print_my_name("Sneha", "Adki")


#Scope
# local variables -> internal variables only inside the functions
# global variables -> overall access entire application


def print_color_red():
    color = "red"
    print(color)


color = "blue"
print(color)
print_color_red()


#key word arguments
def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)


print_numbers(lowest_number=3, highest_number=10)


# with return type of the function
def multiply(a, b):
    return a * b


sol = multiply(3, 4)
print(sol)


# print a list
def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)


number_list = [1, 2, 3, 4, 5]
print_list(number_list)


# calling ftn inside a ftn
def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost):
    current_tax_value = 0.03
    return cost * current_tax_value


final_cost = buy_item(50)
print(final_cost)
