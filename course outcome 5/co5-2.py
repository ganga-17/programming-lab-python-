f1 = open("file1.txt",'r')
str1 = f1.readlines()
f1.close()
f1 = open("file2.txt",'w')
x = 0;
for i in str1:
    x = x+1
    if x%2!=0:
        f1.write(i)
f1.close()
f1=open("test2.txt",'r')
str2=f1.readlines()
print(str2)
