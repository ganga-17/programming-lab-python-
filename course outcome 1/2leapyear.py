a=int(input("enter the current year : "))
b=int(input("enter the final year : "))
print("leap years from ",a," to ",b," are : ")
for i in range(a,b+1):
    if(i%4==0):
        print(i)
