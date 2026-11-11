"""Employee training management application."""

import logging

from employee_training.models import Employee
from employee_training.policies import (
    AdvancedCertificationPolicy,
    StandardCertificationPolicy,
)
from employee_training.services import EmployeeTrainingService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)


def main() -> None:
    """Execute the employee training application."""
    employees = [
        Employee(101, "Rahul", "IT", 90, 85, ["Python", "SQL"]),
        Employee(102, "Priya", "HR", 95, 92, ["Excel"]),
        Employee(103, "Kiran", "IT", 70, 65, ["Python"]),
        Employee(104, "Sneha", "Finance", 98, 95, ["SQL"]),
        Employee(105, "Arjun", "IT", 80, 78, ["Docker"]),
    ]

    service = EmployeeTrainingService(employees)
    standard_policy = StandardCertificationPolicy()
    advanced_policy = AdvancedCertificationPolicy()

    standard_report = service.generate_report(standard_policy)
    advanced_report = service.generate_report(advanced_policy)

    print("\nSTANDARD CERTIFICATION REPORT")
    print(f"Total employees: {standard_report['total_employees']}")
    print(f"Eligible: {standard_report['eligible_employees']}")
    print(f"Not eligible: {standard_report['ineligible_employees']}")
    print(f"Average score: {standard_report['average_score']:.2f}")
    for rank, employee in enumerate(standard_report["ranked_employees"], start=1):
        print(f"{rank}. {employee.name}: {employee.score}")

    print("\nADVANCED CERTIFICATION REPORT")
    print(f"Total employees: {advanced_report['total_employees']}")
    print(f"Eligible: {advanced_report['eligible_employees']}")
    print(f"Not eligible: {advanced_report['ineligible_employees']}")
    print(f"Average score: {advanced_report['average_score']:.2f}")


if __name__ == "__main__":
    main()
