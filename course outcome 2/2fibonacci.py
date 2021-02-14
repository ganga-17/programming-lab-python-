n=int(input("enter the number of terms : "))
a=0
b=1
print("Fibonacci series upto ",n,":")
print(a)
print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)
