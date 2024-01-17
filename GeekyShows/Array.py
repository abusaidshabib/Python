from array import array
array_int = array('i', [101,102,103,104,105])
array_float = array('f', [101,102,103,104,105])

array_int.insert(1, 106) #insert element
array_int.pop() #remove last element
array_int.pop(3) #remove and specific element
array_int.remove(104) #remove specific element
array_int.reverse()
array_int.extend([107,108,109])

#Slicing on array
# new_array_name = array_float[start:stop:stepsize]
new_array_name = array_float[1:4:2]
print(new_array_name)

"""
array_int.append(106)
array_int.append(107)
length = len(array_int)


# print(array_int)
# print(type(array_int))
# print(array_float)

# for value in array_float:
#     print(value)

# for value in range(length):
    # print(value ,"=", array_float[value])
#     print(value = array_float[value])

a = 0
while a < length:
    print(array_int[a])
    a += 1

userInputArray = array('i', [])
n = int(input("Enter Number of Elements: "))

for i in range(n):
    userInputArray.append(int(input("Enter Element: ")))

print(userInputArray)
"""