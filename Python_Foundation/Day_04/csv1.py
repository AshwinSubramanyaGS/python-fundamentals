import csv

with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    print(type(reader))
    for row in reader:
        print(row)