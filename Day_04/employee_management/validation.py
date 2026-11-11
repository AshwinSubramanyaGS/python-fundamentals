import math


def validate_employee(employee: dict) -> bool:

    required_fields = {
        "employee_id",
        "name",
        "department",
        "attendance",
        "score"
    }

    if not isinstance(employee, dict):
        raise ValueError("Employee must be a dictionary.")

    if not required_fields.issubset(employee):
        raise ValueError("Required employee fields are missing.")

    employee_id = employee["employee_id"]
    name = employee["name"]
    attendance = employee["attendance"]
    score = employee["score"]

    if isinstance(employee_id, bool) or not isinstance(employee_id, int):
        raise ValueError("Employee ID must be an integer.")

    if employee_id <= 0:
        raise ValueError("Invalid employee ID.")

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Employee name is required.")

    if not isinstance(employee["department"], str):
        raise ValueError("Invalid department.")

    for field, value in (
        ("attendance", attendance),
        ("score", score)
    ):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{field} must be numeric.")

        if not math.isfinite(value):
            raise ValueError(f"{field} must be finite.")

        if not 0 <= value <= 100:
            raise ValueError(f"Invalid {field}.")

    return True


def is_certification_eligible(employee: dict) -> bool:

    return (
        employee["attendance"] >= 75
        and employee["score"] >= 60
    )