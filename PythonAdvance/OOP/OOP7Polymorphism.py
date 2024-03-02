# Duck Typing

"""
In Python, we follow a principle - If 'it walks like a duck and talks like a duck, it must be a duck' which means python doesn't care about which class of object it is, if it is an object and required behavior is present for that object then it will work. The type of object is distinguished only at runtime. This is called as duck typing.
"""

class Duck:
    def walk(self):
        print("duck walking")
class Horse:
    def walk(self):
        print("Horse walking")
def myfunction(obj):
    obj.walk()

d = Duck()
myfunction(d)