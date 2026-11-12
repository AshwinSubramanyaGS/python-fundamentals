import re

EMPLOYEE_ID_PATTERN = re.compile(r"[A-za-z]{2,}+\d{8}")
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_PATTERN = re.compile(r"[6-9]\d{9}")


def validate_employee_id(employee_id: str) -> bool:
    return EMPLOYEE_ID_PATTERN.fullmatch(employee_id) is not None

def validate_email(email: str) -> bool:
    return EMAIL_PATTERN.fullmatch(email) is not None

def validate_phone(phone: str) -> bool:
    return PHONE_PATTERN.fullmatch(phone) is not None

def main() -> None:
    employee_id = input("Enter employee id: ")
    email = input("Enter employee email: ")
    phone = input("Enter employee phone no: ")
    print("Employee ID:", validate_employee_id(employee_id))
    print("Email:", validate_email(email))
    print("Phone:", validate_phone(phone))


if __name__ == "__main__":
    main()