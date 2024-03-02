"""
-----Main concept of oop----
=====Encapsulation=====
Encapsulation is a concept in programming that involves bundling the data (variables) and methods (functions) that operate on the data into a single unit, known as a class. This unit restricts access to some of its components, protecting the internal details and implementation from external interference. In simpler terms, encapsulation helps in organizing code by keeping related information together and hiding the complex details from the outside, promoting a more modular and secure design.

=====Abstraction=====
Abstraction is the process of simplifying complex systems or ideas by focusing on essential features and ignoring unnecessary details. It involves creating a high-level representation that captures the core aspects of a concept, making it easier to understand and work with. In essence, abstraction allows us to deal with complexity by emphasizing what's important and hiding the intricacies that are not essential for a particular context or task.

=====Inheritance=====
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (subclass or derived class) to inherit characteristics and behaviors from an existing class (superclass or base class). This means that the new class can reuse the code of the existing class, promoting code reusability and establishing a hierarchical relationship between classes. The subclass inherits attributes and methods from the superclass, enabling the creation of a more specialized or extended version of the original class.

=====Polymorphism=====
Polymorphism, in simple terms, refers to the ability of a single function, method, or operator to work with different types of data or objects. It allows a single interface to represent various underlying forms or types, making code more flexible and adaptable. Polymorphism is a key concept in object-oriented programming, enabling code to be written in a more generic and reusable manner.
"""

# Class started-----------
"""
A Python class is a group of attributes and methods

what is attributes?
=== Attributes are represented by variable that contains data.

what is method?
Method performs an action or task.It is similar to function.

class template--
class Classname(object):
    def__init__(self):
        self.variable_name = value
        self.variable_name = 'value'
    def method_name(self):
        Body of Method

here,
    class - class keyword is used to create a class
    object - object represents the base class name from where all classes in python are derived. This class is also derived from object class. This is optional.
    __init__() - This method is used to initialize the variables. This is a special method. WE do not call this method explicitly.
    self - self is a variable which refers to current class instance/object.
"""
