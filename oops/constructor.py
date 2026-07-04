#class Abhi:
    #a = 10 # attribute

    #def hello(self): # method 
        #print("Hello world")
    
    #def arju(self):
        #print("this is method arju")

    #print("this is class abhi")

#print(Abhi().a) # accessing attribute

#Abhi().hello() # accessing method

#obj = Abhi() # creating object of class
#print(obj.a)
#obj.hello()
#obj.arju()

class Abhi:
    def __init__(self, material, color,price): # constructor
        self.material = material # self location 
        self.color = color
        self.price = price

    def show(self): # creating method
        print(f"your object details are Material: {self.material}, Color: {self.color}, Price: {self.price}")

cls = Abhi("leather", "black", 1000) # cls is a class object crete

jiya = Abhi("cotton","blue",200)

cls.show() # calling method
jiya.show()