
def calculate_salary(monthly_salary: float) -> float:
    """calculate and return annual salary"""
    return monthly_salary * 12

annual_salary = calculate_salary(4500.0)

print("Annual Salary : ",annual_salary)