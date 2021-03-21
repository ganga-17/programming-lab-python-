class rectangle:
    def __init__(self,length,breadth) :
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return (2*(self.length+self.breadth))
a=int(input("enter length of rectangle1:"))
b=int(input("enter breadth of rectangle1:"))
e=int(input("enter length of rectangle2:"))
f=int(input("enter breadth of rectangle2:"))
c=rectangle(a,b)
d=rectangle(a,b)
g=rectangle(e,f)
h=rectangle(e,f)
print("area of rectangle 1=",c.area())
print("perimeter of rectangle 1=",d.perimeter())
print("area of rectangle 2=",g.area())
print("perimeter of rectangle 2=",h.perimeter())
if (c.area()>g.area()):
    print("rectangle 1 is larger")
elif (c.area()<g.area()):
    print("rectangle 2 is larger")
else:
    print("area of both rectangles are same")
