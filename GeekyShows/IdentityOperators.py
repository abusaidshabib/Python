#This operator is used to compare whether two objects are same or not. It returns True if memory location of two objects are same else it returns False.

a = 10
b = 10
c = "10"
d = 11
dataList = ["a", 1]
dataList1 = ["a", 1]

print(a is b)
print(a is c)
print(a is d)
print(dataList is dataList1)



print(a is not b)
print(a is not c)
print(a is not d)
print(dataList is not dataList1)