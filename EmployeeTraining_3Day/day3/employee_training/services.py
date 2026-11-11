"""Employee training business operations."""

from collections.abc import Iterable
from typing import TypedDict

from employee_training.decorators import audit_execution
from employee_training.models import Employee
from employee_training.policies import CertificationPolicy


class TrainingReport(TypedDict):
    """Structured certification report returned by the service."""

    total_employees: int
    eligible_employees: int
    ineligible_employees: int
    average_score: float
    ranked_employees: list[Employee]


class EmployeeTrainingService:
    """Manage employees and certification reports."""

    def __init__(self, employees: Iterable[Employee] | None = None) -> None:
        self._employees: dict[int, Employee] = {}
        for employee in employees or []:
            self.add_employee(employee)

    def add_employee(self, employee: Employee) -> None:
        """Register a new employee."""
        if employee.employee_id in self._employees:
            raise ValueError(f"Employee already exists: {employee.employee_id}")
        self._employees[employee.employee_id] = employee

    def get_employee(self, employee_id: int) -> Employee:
        """Retrieve an employee by ID."""
        try:
            return self._employees[employee_id]
        except KeyError as exc:
            raise ValueError(f"Employee not found: {employee_id}") from exc

    def get_all_employees(self) -> list[Employee]:
        """Return employees as a new list."""
        return list(self._employees.values())

    def find_eligible_employees(self, policy: CertificationPolicy)-> list[Employee]:
        """Filter employees using the supplied policy."""
        return [
            employee
            for employee in self._employees.values()
            if policy.is_eligible(employee)
        ]

    def calculate_average_score(self) -> float:
        """Calculate the average score of all employees."""
        if not self._employees:
            return 0.0
        total = sum(employee.score for employee in self._employees.values())
        return total / len(self._employees)

    def rank_employees(self) -> list[Employee]:
        """Return employees ranked by score and then attendance."""
        return sorted(
            self._employees.values(),
            key=lambda employee: (employee.score, employee.attendance),
            reverse=True,
        )

    @audit_execution
    def generate_report(self, policy: CertificationPolicy ) -> TrainingReport:
        """Generate the employee certification summary."""
        employees = self.get_all_employees()
        eligible = self.find_eligible_employees(policy)
        return {
            "total_employees": len(employees),
            "eligible_employees": len(eligible),
            "ineligible_employees": len(employees) - len(eligible),
            "average_score": self.calculate_average_score(),
            "ranked_employees": self.rank_employees(),
        }
