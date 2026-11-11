# Dictionary adding entries

employee = {
    "employee_id": 101,
    "name": "Rahul",
    "department": "IT"
}
employee["assessment_score"] = 85
employee["department"] = "Engineering"
print(employee)

employee.update({
    "attendance": 92,
    "is_active": True,
    "location": "Bengaluru",
    "department": "DevOps"
})


for key, value in employee.items():
    print(f"|{key:<10}|{value:<10}|")
    print("-" *20)