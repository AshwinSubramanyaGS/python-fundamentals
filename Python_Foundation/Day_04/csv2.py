import csv
with open(    "employees.csv",    "r",    newline="",    encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print(type(reader))
        for employee in reader:
                    print(employee["name"])
                    print(employee["department"])
                    print(employee["score"])