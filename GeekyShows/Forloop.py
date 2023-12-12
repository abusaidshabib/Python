"""
value = "MD.Abu Said Shabib"
for ch in value:
    print(ch)

# using range
value = range(1, 10, 2)
for val in value:
    print(val)
value = "MD.Abu Said Shabib"
n = len(value)
for i in range(n):
    print(i, "=", value[i])

# for Loop with else
# The for loop is useful to iterate over the elements of sequence such as string, list, tuple etc. The else suite will be always executed irrespective of the statements in the loop are executed or not.

value = "MD. Abu Said Shabib"
for ch in st:
    print(ch)
else:
    print("Else part")

print("Rest of the Code")

# nested for loop
for i in range(1,5):
    # print("Outer Loop", i)
    for j in range(1,5):
        print(i ,"X", j)

print("Rest of the Code")

for i in range(10):
    if(i == 5):
        break
    print(i)
print("Rest of the code")

for i in range(10):
    if(i == 5):
        continue
    print(i)
print("Rest of the code")
if 1 == 1 :
    pass
elif 0 != 0:
    print("value")
"""