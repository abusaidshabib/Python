# In Python, Numpy is a package which contains classes, functions, variables, large library of mathematical functions etc to work with scientific calculation. Numpy can be used to create n dimensional arrays where n is any integer. We can create 1 dimensional array, 2 dimensional array, 3 dimensional array and so on.
"""
Numpy's array class is called ndarray. It is also known by alias name array. There is another class array in python which is different from numpy's array class.

There are two ways to import numpy:-
== import numpy - This will import the entire numpy module.
== from numpy import * - This will import all class, objects, variable etc from numpy package. Here * means all.

Ways of creating array in numpy
array () Function
linspace () Function
logspace () Function
arange () Function
zeros ()  Function
ones ()  Function


array() Function of numpy module is used to create an array.
Syntax: -
numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

"""
from numpy import *

# Single Row Multiple Columns this called one dimensional array int level array
stu_roll = array([101, 102, 103, 104, 105], int)
name = array(['Abu', 'Said', 'Shabib'], str)
print(type(stu_roll))
print(stu_roll[1])


for value in name:
    print(value)

for