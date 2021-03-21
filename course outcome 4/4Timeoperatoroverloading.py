class Time:
    def __init__(self,h,m,s):
        self.__hour=h
        self.__minute=m
        self.__second=s
    def time(self):
        if self.__second>=60:
            self.__second-=60
            self.__minute+=1
        if self.__minute>=60:
            self.__minute-=60
            self.__hour+=1
    def __add__(self,other):
        self.__hour=self.__hour+other.__hour
        self.__minute=self.__minute+other.__minute
        self.__second=self.__second+other.__second
        return(self.__hour,self.__minute,self.__second)

obj1=Time(3,90,100)
obj1.time()
obj2=Time(6,30,5)
obj2.time()
print("Sum of two time:")
print(obj1+obj2)
