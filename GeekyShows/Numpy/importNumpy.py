# import numpy
from numpy import array, linspace

# Ways of creating Array in numpy
"""
array() Function
linspace() Function
logspace() Function
arrange() Function
zerox() Function
ones() Function
"""

"""
stu_roll =array([101, 102, 103, 104, 105])
stu_roll =array([101, 102, 103, 104, 105], int)
a =array([10.1, 5.2, 4.23, 10.4, 1.5], float)
"""

stu_roll = linspace(1, 8, 5)

# print(stu_roll)

for value in stu_roll:
    print(value)
