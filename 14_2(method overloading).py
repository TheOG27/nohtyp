#Area of rectangle and area of square
class Rectangle():
    def __init__ (self, l, w, s):
        self.length = l
        self.width  = w
        self.side = s
    def a_rs(self):
        return self.length*self.width
    def a_rs(self):
        return self.side*self.side
newSquare = Rectangle(12,10,2)
newRectangle = Rectangle(12,10,2)
print("Area of Square",newSquare.a_rs())
print("Area of Rectangle",newRectangle.a_rs())
