def add(*num):
    z = num[0] + num[1] + num[2]
    return z

print(add(1, 2, 3))


#Keyword variable length arguments
def add(x, **num):
    z = x + num['a']+num['b']
    return z

print(add(3, a=4,b=5))