l1=[1,5,7,3,9]
l2=[2,4,8,1,9]
a=set(l1)
b=set(l2)
c=a.intersection(b)
if(c!=0):
    print("values occur in both the list are ",c)
