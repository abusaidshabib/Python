# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))

# if height > 120:
#     print("you can ride the rollercoaster!")
# else:
#     print("Sorry , you have to grow taller before you can ride.")

# number = int(input())

# if number % 2 > 0:
#     print("This is an odd number")
# else:
#     print("this is an even number")

# height = int(input("Enter your height in cm"))
# age = int(input("Enter your age only rounded year"))

# if height > 120:
#     if age > 18:
#         print("you have to pay $12")
#     elif age < 18:
#         print("you have to pay $7")
# else:
#     print("you are not allow")

height = float(input("Enter your height in miter"))
weight = float(input("Enter your weight in KG"))


bmi = weight/(height*height)
print(bmi)
if bmi < 18.5:
    print("You are underweight")
elif 18.5<= bmi < 25:
    print("You have a normal weight")
elif 25 <= bmi < 30:
    print("You are slightly overweight")
elif 30 <= bmi <35:
    print("You are obese")
elif 35 > bmi:
    print("You are clinically obese")