from numpy import zeros
m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))
a = zeros((m, n))

for i in range(len(a)):
    for j in range(len(a[i])):
        x = int(input("Enter Element: "))
        a[i][j] = x

print(a)