class Animal:
    name = "Tiger"  # class attribute

    def __init__(self, age):
        self.age = age # instance attribute location

    def show(self): # instance method
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod
    def class_method(cls): # class method (cls) are to target the class 
        print("this is a class method")
    
    @staticmethod
    def static_method(): # static method (NOT targerting the class or instance)
        print("this is a static method")

obj = Animal(10)
obj.show() # instance method call
obj.class_method() # class method call
obj.static_method() # static method call