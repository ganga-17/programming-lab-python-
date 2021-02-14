l1=[10,20,30,40]
l2=[10,30,50]
s1=0
s2=0
for i in l1:
    s1=s1+i
for j in l2:
    s2=s2+j
if(s1==s2):
    print("lists sums same")
else:
    print("lists sums different")
