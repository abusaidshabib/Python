# if statement = a block of code that will execute if it's condition is true

age = int(input("how old are you?: "))
if age >= 18:
    if age == 100:
        print("You are a century old")
    else:
        print("You are and adult")
elif age < 18:
    if age < 1:
        print("You are don't exist")
    else:
        print("You are a child")
else:
    print("You don't belong here")


# Replace ___ with your code

# create variable number1 with value 9
number1 = int(input("Enter first number"))

# create variable number2 with value 5
number2 = int(input("Enter second number"))

# add number1 and number2
result = number1 + number2

# print result
print(result)