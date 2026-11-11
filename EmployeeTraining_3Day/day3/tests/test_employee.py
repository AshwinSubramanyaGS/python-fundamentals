"""Tests for the employee training application."""

import pytest

from day3.employee_training.models import Employee
from day3.employee_training.policies import (
    AdvancedCertificationPolicy,
    StandardCertificationPolicy,
)
from day3.employee_training.services import EmployeeTrainingService


def create_employee() -> Employee:
    """Build a sample employee for tests."""
    return Employee(
        employee_id=101,
        name="Rahul",
        department="IT",
        attendance=90,
        score=85,
        skills=["Python"],
    )


def test_employee_creation() -> None:
    employee = create_employee()
    assert employee.name == "Rahul"
    assert employee.score == 85


def test_employee_name_is_trimmed() -> None:
    employee = Employee(102, " Priya ", " HR ", 90, 80)
    assert employee.name == "Priya"
    assert employee.department == "HR"


def test_invalid_score() -> None:
    with pytest.raises(ValueError):
        Employee(102, "Priya", "HR", 90, 120)


def test_non_finite_score() -> None:
    with pytest.raises(ValueError):
        Employee(103, "Kiran", "IT", 90, float("nan"))


def test_standard_policy() -> None:
    assert StandardCertificationPolicy().is_eligible(create_employee())


def test_advanced_policy() -> None:
    assert AdvancedCertificationPolicy().is_eligible(create_employee())


def test_duplicate_employee() -> None:
    employee = create_employee()
    service = EmployeeTrainingService([employee])
    with pytest.raises(ValueError):
        service.add_employee(employee)


def test_get_employee() -> None:
    service = EmployeeTrainingService([create_employee()])
    assert service.get_employee(101).name == "Rahul"


def test_missing_employee() -> None:
    service = EmployeeTrainingService()
    with pytest.raises(ValueError, match="Employee not found"):
        service.get_employee(999)


def test_empty_service_average_is_zero() -> None:
    assert EmployeeTrainingService().calculate_average_score() == 0.0


def test_average_score() -> None:
    employees = [
        create_employee(),
        Employee(102, "Priya", "HR", 95, 95),
    ]
    service = EmployeeTrainingService(employees)
    assert service.calculate_average_score() == 90.0


def test_report_counts() -> None:
    service = EmployeeTrainingService(
        [
            create_employee(),
            Employee(102, "Kiran", "IT", 70, 65),
        ]
    )
    report = service.generate_report(StandardCertificationPolicy())
    assert report["total_employees"] == 2
    assert report["eligible_employees"] == 1
    assert report["ineligible_employees"] == 1
