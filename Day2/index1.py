# value = str(1234)
# print(len(value))
# print("Hello"[1])
# print(type(value))

# inputValue = input()
# print(int(inputValue[0])+int(inputValue[1]))
# print(2**3)

# calculation sequence - parentheses> exponents> multiplication> division> addition> subtraction
# print(3*3+3/3-3)

# challenge2
# height = float(input())
# weight = float(input())

# BMI =  weight/(height*height)
# print(BMI)

# print(round(8/3))
# print(round(8/3, 2))
# print(8//3)
# print(5//2)

# 52 weeks in year
# age = int(input())
# temp = (90 - age)*52
# print(temp)

total = float(input("What was the total bill?"))
valid_value = [10, 12, 15]

while True:
    tips = float(input("Enter percentage tip would you like to give? 10, 12, or 15?"))
    if tips in valid_value:
        break
    else:
        tips = int(input("Enter percentage tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people to split the bill?"))
result = (float(total + ((tips/100)*total)))/people
print(round(result, 2))
print("{:.2f}".format(result, 2))