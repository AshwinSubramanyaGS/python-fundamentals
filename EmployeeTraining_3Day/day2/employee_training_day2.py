"""Employee training management using Python collections.

Day 2: lists, tuples, sets, dictionaries, comprehensions, filtering, grouping,
lookup, sorting, zip and summary calculations.
"""

# Step 1 – Maintain employee names and scores.
employee_names = ["Rahul", "Priya", "Kiran", "Sneha", "Arjun"]
assessment_scores = [85, 92, 65, 95, 78]

print("\nSTEP 1 – EMPLOYEE SCORES")
for name, score in zip(employee_names, assessment_scores, strict=True):
    print(f"{name}: {score}")

# Step 2 – Fixed training configuration.
training_configuration = ("Python Foundation", 75, 60, 100)
course_name, minimum_attendance, passing_score, maximum_score = training_configuration

print("\nSTEP 2 – TRAINING CONFIGURATION")
print(f"Course: {course_name}")
print(f"Attendance requirement: {minimum_attendance}%")
print(f"Passing score: {passing_score}")
print(f"Maximum score: {maximum_score}")

# Step 3 – Identify unique departments.
departments = ["IT", "HR", "IT", "Finance", "Engineering", "HR"]
unique_departments_from_sample = set(departments)
print("\nSTEP 3 – UNIQUE DEPARTMENTS")
print(sorted(unique_departments_from_sample))

# Step 4 and 5 – Represent one employee and multiple employee records.
employee = {
    "employee_id": 101,
    "name": "Rahul",
    "department": "IT",
    "attendance": 90,
    "assessment_score": 85,
    "skills": ["Python", "SQL"],
}
print("\nSTEP 4 – SINGLE EMPLOYEE")
print(employee["name"])
print(employee["department"])
print(employee.get("manager", "Unassigned"))

employees = [
    {
        "employee_id": 101,
        "name": "Rahul",
        "department": "IT",
        "attendance": 90,
        "assessment_score": 85,
        "skills": ["Python", "SQL"],
    },
    {
        "employee_id": 102,
        "name": "Priya",
        "department": "HR",
        "attendance": 95,
        "assessment_score": 92,
        "skills": ["Excel", "Communication"],
    },
    {
        "employee_id": 103,
        "name": "Kiran",
        "department": "IT",
        "attendance": 70,
        "assessment_score": 65,
        "skills": ["Python", "Linux"],
    },
    {
        "employee_id": 104,
        "name": "Sneha",
        "department": "Finance",
        "attendance": 98,
        "assessment_score": 95,
        "skills": ["Excel", "SQL"],
    },
    {
        "employee_id": 105,
        "name": "Arjun",
        "department": "IT",
        "attendance": 80,
        "assessment_score": 78,
        "skills": ["Docker", "Git"],
    },
]

print("\nSTEP 5 – EMPLOYEE RECORDS")
for record in employees:
    print(f"{record['employee_id']}: {record['name']}")

# Step 6 – Build a lookup dictionary and reject duplicate IDs.
employee_by_id = {}
for record in employees:
    employee_id = record["employee_id"]
    if employee_id in employee_by_id:
        raise ValueError(f"Duplicate employee ID: {employee_id}")
    employee_by_id[employee_id] = record

search_id = 103
found_employee = employee_by_id.get(search_id)
print("\nSTEP 6 – EMPLOYEE LOOKUP")
if found_employee is not None:
    print(found_employee)
else:
    print("Employee not found")

# Step 7 – Filter certification-eligible employees.
eligible_employees = [
    record
    for record in employees
    if record["attendance"] >= minimum_attendance
    and record["assessment_score"] >= passing_score
]
print("\nSTEP 7 – ELIGIBLE EMPLOYEES")
for record in eligible_employees:
    print(record["name"])

# Step 8 – Identify high-performing employees.
high_performers = [
    record for record in employees if record["assessment_score"] >= 85
]
print("\nSTEP 8 – HIGH PERFORMERS")
for record in high_performers:
    print(record["name"], record["assessment_score"])

# Step 9 – Create an employee score mapping.
employee_scores = {
    record["employee_id"]: record["assessment_score"] for record in employees
}
print("\nSTEP 9 – EMPLOYEE SCORE MAPPING")
print(employee_scores)

# Step 10 – Group employees by department.
department_groups = {}
for record in employees:
    department = record["department"]
    department_groups.setdefault(department, []).append(record["name"])

print("\nSTEP 10 – DEPARTMENT GROUPS")
for department, names in sorted(department_groups.items()):
    print(f"{department}: {names}")

# Step 11 – Identify unique technical skills.
unique_skills = {
    skill for record in employees for skill in record["skills"]
}
print("\nSTEP 11 – UNIQUE TECHNICAL SKILLS")
for skill in sorted(unique_skills):
    print(skill)

# Step 12 – Generate a sorted performance report.
ranked_employees = sorted(
    employees,
    key=lambda record: record["assessment_score"],
    reverse=True,
)
print("\nSTEP 12 – EMPLOYEE PERFORMANCE RANKING")
for rank, record in enumerate(ranked_employees, start=1):
    print(f"{rank}. {record['name']} - {record['assessment_score']}")

# Step 13 – Generate the summary.
total_employees = len(employees)
total_score = sum(record["assessment_score"] for record in employees)
average_score = total_score / total_employees if total_employees else 0.0
eligible_count = len(eligible_employees)
eligibility_percentage = (
    eligible_count / total_employees * 100.0 if total_employees else 0.0
)
unique_departments = {record["department"] for record in employees}

print("\n========== TRAINING SUMMARY ==========")
print(f"Total employees: {total_employees}")
print(f"Eligible employees: {eligible_count}")
print(f"Not eligible: {total_employees - eligible_count}")
print(f"Average assessment score: {average_score:.2f}")
print(f"Certification eligibility: {eligibility_percentage:.2f}%")
print(f"Unique departments: {len(unique_departments)}")
print(f"Unique technical skills: {len(unique_skills)}")
