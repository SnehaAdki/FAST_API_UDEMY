"""
Lists []
"""

lists = [80,90,72,100,8]
print(lists)

people_list = ["Sneha" , "Vj" , "Sheetal", "Shweta"]
print(people_list)
print(people_list[-1])

people_list[1] = "Vijay"
print(people_list)

print(len(people_list))
print(people_list[0:2])
print(people_list[:3])
print(people_list[:])

#-- insert
lists.append(10000)
print(lists)
lists.insert(2,9000)
print(lists)
lists.remove(9000)
print(lists)
lists.pop(0)
print(lists)
lists.sort()
print(lists)