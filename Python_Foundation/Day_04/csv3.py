import csv

employees = [
    [101, "Lakshmi", "IT", 90, 85],
    [102, "Tulasi", "HR", 95, 92],
    [103, "Meghana", "IT", 70, 65],
]
with open("employee_report.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["employee_id", "name", "department", "attendance", "score"])
    writer.writerows(employees)
