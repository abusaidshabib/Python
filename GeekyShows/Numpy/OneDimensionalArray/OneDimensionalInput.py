from numpy import zeros
n = int(input("enter Number of Elements: "))
a = zeros(n, dtype=int)
for i in range(len(a)):
    x = int(input("Enter Elements: "))
    a[i] = x

print(a)