from numpy import array, where, nonzero
a = array([101, 102, 103, 104, 105])
b = array([100, 200, 300, 400, 500])
a[1] = 80

"""
result = where (a>b, a, b)
result2 = nonzero(a)
print(result, result2)
"""

c = a.view()
print(a)
print(b)
print("a", id(a))
print("b", id(b))
