#Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square
a=int(input("Enter the upper limit="))
b=int(input("Enter the lower limit="))
li1=[]
li2=[]

for x in range(b, a + 1):
    if x % 2 == 0:
        li1.append(x)

for y in li1:
    for z in range(1,y):
          if (z*z) ==y:
             li2.append(y)
print(li2)
