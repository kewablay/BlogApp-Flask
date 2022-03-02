import csv

with open('TechCrunch1.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    print(reader)
    next(reader) # skip the header line
for row in reader:
    print(row)
