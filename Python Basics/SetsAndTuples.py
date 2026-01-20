#
# "Set" {}
#
my_set = {1, 2, 3, 4,5}

print(my_set)

my_set = {1, 2, 3, 4,5,6,71,2,3,4,5,"aaa"}
print(my_set)
print(type(my_set))
print(len(my_set))

for x in my_set:
    print(x,end=" ")
print(end ="\n")
# Throws an error
# print(my_set[0])

print("Removed the elements")
my_set.discard("aaa")
print(my_set)

my_set.clear()
print(my_set)

my_set.add("aaabbb")
print(my_set)
my_set.update(["aaa","bbb"])
print(my_set)


"""
Tuple ()
"""

my_tuple = (1, 2, 3,4,5,6,11,1)
print(my_tuple)
print(type(my_tuple))
print(len(my_tuple))
print(my_tuple[0])