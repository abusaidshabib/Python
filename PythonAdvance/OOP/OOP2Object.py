# Object is class type variable or class instance. To use a class, we should create an object to the class. Instance creation represents allotting memory necessary to store the actual data of the variables. Each time you create an object of a class a copy of each variables defined in the class in created. In other words you can say that each object of a class has its own copy data members defined in the class.
"""
Syntax: -
object_name = class_name()

how it works
-------------

# class Mobile: 
#     def__init__(self, m):
#         self.model = m
#     def show_model (self):
#         print('Model:', self.model)

# realme = Mobile('RealMe x')

- A block of memory is allocated on heap. The size of allocated memory is to be decided from the attributes and methods available in the class(Mobile).
- After allocating memory block, the special method__init__() is called internally. This method stores the initial data into the variables.
- The allocated memory location address of the instance is returned into object(realme).
- The memory location is passed to self.
"""

# self variable
"""
self is a default variable that contains the memory address of the current object. This variable is used to refer all the instance variable and method. When we create object of a class, the object name contains the memory location of hte object. This memory location is internally passed to self, as self knows the memory address of the object so we can access variable and method of object.
"""

#Object
"""
Each time you create an object of a class a copy of each variables defined in the class is created.
# class Mobile: 
#     def__init__(self, m):
#         self.model = m
#     def show_model (self):
#         print('Model:', self.model)

# realme = Mobile('RealMe x')
# realme = Mobile('RealMe y')
# realme = Mobile('RealMe z')
"""

"""
#Example 1
# class name must be start with capital
class My_class(object):
    def show(self):
        print("I am a Method")

x = My_class()
x.show()

#Example 2
# writing object like (object) is not mandatory
class My_class:
    def show(self):
        print("I am a Method")

x = My_class()
x.show()

#Example 3
class Mobile:
    def __init__(self):
        self.model = 'RealMe x'
    
    def show_model(self):
        print("Model: ", self.model)

realme = Mobile()
realme.show_model()
#access object variable
print(realme.model)
#reassign a value on variable
realme.model = 'RealMe Pro2'
print(realme.model)
"""



#Example 4
class Mobile:
    def __init__(self, model):
        self.model = model
    
    def show_model(self, price):
        # price = price 
        #or
        self.price = price 
        print("Model: ", self.model, "Price: ", self.price)

realme = Mobile('RealMe X')
realme.show_model(1000)

print(id(realme))
print()
redmi = Mobile('Redmi 7s')
redmi.show_model(2000)
print(id(redmi))
print()
geek = Mobile('Python')
geek.show_model(49)
print(id(geek))
