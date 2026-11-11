from .database import (
    get_all_employees,
    department_report,
    course_report
)

from .imports import export_json, export_eligible_csv


def display_employees():

    employees = get_all_employees()

    print("\nEMPLOYEE DIRECTORY")

    for employee in employees:

        print(
            employee["employee_id"],
            employee["name"],
            employee["department"],
            employee["score"]
        )


def display_department_report():

    print("\nDEPARTMENT PERFORMANCE")

    for row in department_report():

        print(
            row["department"],
            "Employees:", row["employee_count"],
            "Average:", round(row["average_score"], 2),
            "Highest:", row["highest_score"]
        )


def display_course_report():

    print("\nCOURSE PERFORMANCE")

    for row in course_report():

        print(
            row["name"],
            row["course_name"],
            row["score"]
        )



def generate_reports():

    employees = get_all_employees()

    # Convert SQLite Row objects into dictionaries
    employee_data = [
        dict(employee)
        for employee in employees
    ]

    export_json(
        employee_data,
        "employee_report.json"
    )

    export_eligible_csv(
        employee_data,
        "eligible_employees.csv"
    )

    print("\nReports generated successfully.")