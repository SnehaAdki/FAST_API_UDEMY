# Create a list of 5 animals called zoo
#
# - Delete the animal at the 3rd index.
#
# - Append a new animal at the end of the list
#
# - Delete the animal at the beginning of the list.
#
# - Print all the animals
#
# - Print only the first 3 animals


animals = ["Tiger" , "Lion", "Zebra", "Panda", "Cheeta"]
animals.pop(3)
animals.append("Elephant")
animals.pop(0)
print(animals)
for x in animals:
    print(x)
print(animals[:3])