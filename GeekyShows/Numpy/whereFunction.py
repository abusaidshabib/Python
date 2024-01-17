from numpy import array, where, nonzero
a = array([101, 102, 103, 104, 105])
b = array([100, 200, 300, 400, 500])

result = where (a>b, a, b)
result2 = nonzero(a)
print(result, result2)

