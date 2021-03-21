class A:
    __length=0
    __breadth=0
    __area=0
    def __init__(self,l,w):
        self.__length=l
        self.__breadth=w
    def rectarea(self):
        self.__area=self.__length*self.__breadth
    def __lt__(self,other):
        if(self.__area<other.__area):
            return True
        else:
            return False
ob1=A(10,20)
ob1.rectarea()
ob2=A(40,10)
ob2.rectarea()
if ob1<ob2:
    print("ob1 is smaller")
else:
    print("ob2 is smaller")
        
