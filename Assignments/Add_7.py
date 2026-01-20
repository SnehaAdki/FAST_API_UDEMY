# - Create a function that takes in 3 parameters(firstname, lastname, age) and
#
# returns a dictionary based on those values


def create_dict(firstname , lastname, age):
    return { "firstname": firstname, "lastname": lastname, "age": age}


dict_created = create_dict(firstname = "John", lastname = "Smith", age = 20)
print(dict_created)


dict_created = create_dict( lastname = "Adki", age = 30, firstname = "Sneha")
print(dict_created)