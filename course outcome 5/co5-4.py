import csv
f=open("flowers.csv","w")
writer=csv.DictWriter(f,fieldnames=["flower","count"])
writer.writeheader()#writeheader() write headers to the csvfile
writer.writerow({"flower":"rose","count":"1"})
writer.writerow({"flower":"lilly","count":"2"})
writer.writerow({"flower":"lotus","count":"3"})
writer.writerow({"flower":"sunflower","count":"4"})
f.close()
c=0
f=open("flowers.csv")
reader=csv.DictReader(f)
for row in reader:
    if c==0:
        print(f'{" ".join(row)}')
    print(f'{row["flower"]},{row["count"]}')
f.close()
