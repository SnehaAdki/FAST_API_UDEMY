"""
For and While Loops
"""


my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(num, end=" ")

print("")

for x in range(0,len(my_list)):
    print(my_list[x],end=" ")

print("")
print("Total is")
total = 0
for x in range(0,len(my_list)):
    total = total + my_list[x]
    
print(total)

week_days =  ["Monday" , "Tuesday","Wednesday","Thursday","Friday"]
for x in range(0,len(week_days)):
    print(f"Happy {week_days[x]}")

i = 10
while i < 20:
    print(i, end=" ")
    i+=1

"""
continue
"""
i=0
while i < 5:
    i+=1
    if i == 3:
        continue
    print(i, end=" ")
else:
    print("OOOOOO now i is greater then  or equal to 5")

"""
continue
"""
i=0
while i < 5:
    i+=1
    if i == 3:
        continue
    print(i, end=" ")
    if i == 4:
        break
else:
    print("OOOOOO now i is greater then  or equal to 5")


