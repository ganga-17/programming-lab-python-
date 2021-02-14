str1=str(input("enter a string : "))
length = len(str1)
if length > 0:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'
    print(str1)

