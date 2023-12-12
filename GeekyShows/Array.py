""" 
import array
array = [1, 2, 3, 4, 5, 6, 7]
for i in array:
    print(i) 
stu_roll = array.array('i', [1, 2, 3, 4, 5, 6, 7])
for element in stu_roll:
    print(element)
"""



from array import *
stu_roll = array('i', [1, 2, 3, 4, 5, 6, 7])
print(type(stu_roll))
for element in stu_roll:
    print(element)