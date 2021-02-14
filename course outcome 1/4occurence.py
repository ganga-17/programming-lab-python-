n=str(input("enter a line of text : "))
a=n.split()
s2=[]
for i in a:
    if i not in s2:
        s2.append(i)
for i in range(0,len(s2)):
    print("count of ",s2[i],"is",a.count(s2[i]))
    
