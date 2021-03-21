F1=open("file1.txt",'w')
F1.close()
F1 = open("file1.txt",'r')
F2 = list()
for line in F1:
      F2.append(line)
print(F2)
