from numpy import array
a = array([101, 102, 103, 104, 105])
c = array([101, 102, 103, 104, 105])
print(a==c)
print(a<c)
#any operation could done
a = a + 5
print(a)


b = array([1, 2, 3, 4, 5])
a = c+b
print(a)
print(a==c)
print(a<c)
print(any(a==c))
print(all(a==c))
