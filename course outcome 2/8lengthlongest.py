l=['hello','honest','here','hai','human being']
a=len(l[0])
b=l[0]
for i in l:
    if len(i)>a:
        a=len(i)#length of the longest word
        b=i#longest word
print("The length of the longest word in the list is ",a)
