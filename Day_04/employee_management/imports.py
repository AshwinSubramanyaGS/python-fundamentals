import csv
import json

from pathlib import Path

from .validation import validate_employee


def import_csv(file_path):

    employees = []

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open(
        "r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        expected_fields = {
            "employee_id",
            "name",
            "department",
            "attendance",
            "score",
            "course"
        }

        if not expected_fields.issubset(reader.fieldnames or []):
            raise ValueError("Invalid CSV structure.")

        for row_number, row in enumerate(reader, start=2):

            try:

                employee = {
                    "employee_id": int(row["employee_id"]),
                    "name": row["name"].strip(),
                    "department": row["department"].strip(),
                    "attendance": float(row["attendance"]),
                    "score": float(row["score"]),
                    "course": row["course"].strip()
                }

                validate_employee(employee)

                if not employee["course"]:
                    raise ValueError("Course name is required.")

                employees.append(employee)

            except (ValueError, TypeError) as error:

                raise ValueError(
                    f"Invalid CSV row {row_number}: {error}"
                ) from error

    return employees


def export_json(employees, output_path):

    with Path(output_path).open(
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            employees,
            file,
            indent=4,
            ensure_ascii=False,
            allow_nan=False
        )


def import_json(file_path):

    path = Path(file_path)

    try:

        with path.open("r", encoding="utf-8") as file:

            employees = json.load(file)

        if not isinstance(employees, list):
            raise ValueError("JSON must contain an employee list.")

        for employee in employees:
            validate_employee(employee)

        return employees

    except FileNotFoundError:

        print("JSON file not found.")

        raise

    except json.JSONDecodeError as error:

        print(f"Invalid JSON: {error}")

        raise


def export_eligible_csv(employees, output_path):

    fieldnames = [
        "employee_id",
        "name",
        "department",
        "attendance",
        "score"
    ]

    def sanitize(value):

        text = str(value)

        if text.lstrip().startswith(("=", "+", "-", "@")):
            return "'" + text

        return text

    with Path(output_path).open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for employee in employees:

            if (
                employee["attendance"] >= 75
                and employee["score"] >= 60
            ):

                safe_employee = {
                    field: sanitize(employee[field])
                    if field in ("name", "department")
                    else employee[field]
                    for field in fieldnames
                }

                writer.writerow(safe_employee)