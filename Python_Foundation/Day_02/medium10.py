employees = [
    {"name": "Rahul", "score": 85, "attendance": 90},
    {"name": "Priya", "score": 95, "attendance": 85},
    {"name": "Kiran", "score": 85, "attendance": 95},
    {"name": "Sneha", "score": 95, "attendance": 98},
]
ranked_employees = sorted(
    employees,
    key=lambda employee: (employee["score"], employee["attendance"]),
    reverse=True,
)
for rank, employee in enumerate(ranked_employees, start=1):
    print(rank, employee["name"], employee["score"], employee["attendance"])
