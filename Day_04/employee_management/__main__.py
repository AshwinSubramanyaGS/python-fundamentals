from pathlib import Path

from .database import (
    initialize_database,
    bulk_insert_employees,
    create_course,
    enroll_employee,
    get_employee,
    update_employee_score,
    transfer_score_transaction
)

from .imports import import_csv

from .reporting import (
    display_employees,
    display_department_report,
    display_course_report,
    generate_reports
)


def main():

    print("EMPLOYEE TRAINING MANAGEMENT SYSTEM")

    initialize_database()

    csv_path = Path("data/employees.csv")

    employees = import_csv(csv_path)

    try:

        bulk_insert_employees(employees)

        print("\nEmployees imported successfully.")

    except Exception as error:

        print(f"\nImport skipped or failed: {error}")

        # A repeated run will encounter duplicate IDs.
        # Existing records remain unchanged.

    # Create courses and employee enrollments.

    for employee in employees:

        create_course(employee["course"])

        try:

            enroll_employee(
                employee["employee_id"],
                employee["course"],
                employee["score"]
            )

        except Exception as error:

            print("Enrollment skipped:", error)

    # READ

    display_employees()

    # UPDATE

    employee = get_employee(101)

    if employee:

        update_employee_score(101, 95)

        print("\nEmployee score updated.")

    # Transaction rollback demonstration

    transfer_score_transaction()

    # Reports

    display_department_report()

    display_course_report()

    generate_reports()


if __name__ == "__main__":

    main()