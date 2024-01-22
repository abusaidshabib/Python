sum = lambda x:x+1
print(sum(5))

add = lambda x,y:x+y
print(add(5,2))

# nested lambda function
add = lambda x=10:(lambda y: x+y)
a = add()
print(a(20))