c1=['red','orange','white','black','green']
print("color list1=",c1)
c2=['blue','violet','yellow','brown','black','white']
print("color list2=",c2)
a=set(c1)
b=set(c2)
print("common elements=",a.intersection(b))
print("colors in c1 not contaained in c2=",a-b)
