mystring = 'abcdefg'

# [start:end:steps]
print(mystring[2])
print(mystring[2:])
print(mystring[:2])
print(mystring[::2])
value = mystring.lower()
print(mystring.upper(), value)
x = mystring.split('e')
print(x)

# Print Formatting
newvalue = "Insert another string here: {}".format("INSERT ME!")
newvalue2 = "Item One: {} Insert another string here: {}".format("INSERT ME!", "Cat")
newvalue3 = "Item One: {x} Insert another string here: {y}".format(x = "INSERT ME!", y ="Cat")
print(newvalue2)