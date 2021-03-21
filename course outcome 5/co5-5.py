import csv
csv_rows = ['No','Name','Color']
dict_data = [
{'No': 1, 'Name': 'Rose', 'Color': 'Red'},
{'No': 2, 'Name': 'Jasmine', 'Color': 'white'},
{'No': 3, 'Name': 'Lotus', 'Color': 'Rose'},
{'No': 4, 'Name': 'Sunflower', 'Color': 'Yellow'},
{'No': 5, 'Name': 'Hibiscus', 'Color': 'Red'},
]
csv_file = "flowers.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_rows)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)


with open('flowers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
