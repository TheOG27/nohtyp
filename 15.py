#simple inheritance
class fruit:
    print("hello from parent class")
    def mango(self):
        print("it is a mango")
    def apple(self):
        print("it is a apple")
class display(fruit):
    print("hello from child class")

d=display()
d.mango()
d.apple()

#multiple inheritance
class add:
    def addition(self,a,b):
        return a+b
class mul:
    def multiplication(self,x,y):
        return x*y
        
class opertions(add,mul):
    def divide(self,a,b):
        return a/b
    
o=opertions()
print("Addtion is :",o.addition(10,20))
print("Multiplication is :",o.multiplication(10,2))
print("Division is :",o.divide(50,5))





