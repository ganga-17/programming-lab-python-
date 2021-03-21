import csv
with open('film1.csv','w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(["SN","Movie","Rating"])
    writer.writerow([1,"Lord of the Rings",5])
    writer.writerow([2,"Harrypotter",6])
    writer.writerow([3,"Romeo and juliet",7])
    writer.writerow([4,"Lion king",8])
with open('film1.csv')as csvfile:
    data=csv.reader(csvfile)
    for row in data:
        print(','.join(row))
