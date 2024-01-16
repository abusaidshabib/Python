array1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 1, 2]
number = 20

result = []
array1[0] += number
result.append(array1[0])
array1.pop(0)
for value in array1:
    result.append(value + result[-1])

print(result)
