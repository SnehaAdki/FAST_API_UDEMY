"""
dictionary
"""

user_dict ={
    "user_name" : "Sneha_123",
    "name" : "Seha",
    "age" : 25,
}

print(user_dict)
# print(user_dict["user_name"])
print(user_dict.get("user_name"))
user_dict["married"] = True
print(user_dict)
print(len(user_dict))
user_dict.pop("age")
print(user_dict)

# user_dict.clear()
print(user_dict)
# del user_dict
# print(user_dict) this never exist after delete


for x in user_dict:
    print(x)


for key,val in user_dict.items():
    print(f"Key is {key} and Value is {val}")


#removs from both dict
user_dict2 = user_dict
user_dict2.pop("name")
print(user_dict2)
print(user_dict)


#copy() don't remove identical w.r.t memory
user_dict1 = {
    "user_name" : "Sneha_123",
    "name" : "Seha",
    "age" : 25,
}
user_dict2 = user_dict1.copy()
user_dict2['user_name'] = "SVJ"
print(user_dict2)
print(user_dict1)