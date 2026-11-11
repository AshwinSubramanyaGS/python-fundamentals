#requires -Version 5.1
<#
Creates the complete three-day Employee Training Management System training project.
Run this script from the parent directory where you want the project created.

The script reuses an active virtual environment, or detects .venv / venv in the
current directory or parent directory. It does not delete or recreate the venv.
#>

$ErrorActionPreference = "Stop"
$ProjectName = "EmployeeTraining_3Day"
$ProjectRoot = Join-Path (Get-Location) $ProjectName

function Write-ProjectFile {
    param(
        [Parameter(Mandatory = $true)][string]$RelativePath,
        [Parameter(Mandatory = $true)][string]$Content
    )
    $FullPath = Join-Path $ProjectRoot $RelativePath
    $Parent = Split-Path -Parent $FullPath
    if (-not (Test-Path $Parent)) {
        New-Item -ItemType Directory -Path $Parent -Force | Out-Null
    }
    Set-Content -LiteralPath $FullPath -Value $Content -Encoding UTF8
    Write-Host "Created: $RelativePath" -ForegroundColor DarkGray
}

Write-Host "`n=== Employee Training Management System: 3-Day Setup ===" -ForegroundColor Cyan

# Locate and reuse the existing virtual environment.
$PythonExe = $null
if ($env:VIRTUAL_ENV) {
    $Candidate = Join-Path $env:VIRTUAL_ENV "Scripts\python.exe"
    if (Test-Path $Candidate) { $PythonExe = $Candidate }
}
if (-not $PythonExe) {
    $Candidates = @(
        (Join-Path (Get-Location) ".venv\Scripts\python.exe"),
        (Join-Path (Get-Location) "venv\Scripts\python.exe"),
        (Join-Path (Split-Path (Get-Location) -Parent) ".venv\Scripts\python.exe"),
        (Join-Path (Split-Path (Get-Location) -Parent) "venv\Scripts\python.exe")
    )
    foreach ($Candidate in $Candidates) {
        if (Test-Path $Candidate) { $PythonExe = $Candidate; break }
    }
}
if (-not $PythonExe) {
    throw "Could not find your existing venv. Activate it first, or run this script from the folder containing .venv or venv."
}

Write-Host "Using Python: $PythonExe" -ForegroundColor Green
& $PythonExe --version
if ($LASTEXITCODE -ne 0) { throw "Python could not be executed from the detected virtual environment." }

# Create project folders.
$Directories = @(
    "day1",
    "day2",
    "day3\employee_training",
    "day3\tests"
)
foreach ($Directory in $Directories) {
    New-Item -ItemType Directory -Path (Join-Path $ProjectRoot $Directory) -Force | Out-Null
}

Write-ProjectFile "requirements-dev.txt" @'
ruff
bandit
pytest
mypy
'@

Write-ProjectFile "pyproject.toml" @'
[tool.ruff]
line-length = 88
target-version = "py310"
exclude = [".venv", "venv", "build", "dist", "__pycache__"]

[tool.ruff.lint]
select = ["E", "F", "W", "I", "B", "UP"]
ignore = []

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

[tool.mypy]
python_version = "3.10"
strict = true
warn_unused_configs = true
show_error_codes = true

[tool.pytest.ini_options]
testpaths = ["day3/tests"]
python_files = ["test_*.py"]
pythonpath = ["day3"]
addopts = "-ra"

[tool.bandit]
exclude_dirs = ["day3/tests", ".venv", "venv"]
'@

Write-ProjectFile "README.md" @'
# Employee Training Management System – Three-Day Python Lab

## Environment
This project uses the existing Python virtual environment. Activate it before running
commands if it is not already active.

## Install development tools
```powershell
python -m pip install -r requirements-dev.txt
```
The setup script installs Ruff, Bandit and pytest and retains mypy.

## Day 1 – Fundamentals
```powershell
python day1/employee_training.py
```

## Day 2 – Collections
```powershell
python day2/employee_training_day2.py
```

## Day 3 – Object-oriented refactoring
Run from the project root:
```powershell
python day3/main.py
```

Run tests:
```powershell
python -m pytest day3/tests -q
```

## Quality checks
Run from the project root:
```powershell
ruff check .
ruff format --check .
mypy --strict --mypy-path day3 day3/employee_training day3/main.py
bandit -r day3/employee_training
```

To apply formatting:
```powershell
ruff format .
```

## Learning progression
- Day 1 intentionally avoids lists, dictionaries, functions and classes.
- Day 2 introduces Python collections and collection operations.
- Day 3 refactors the same business problem into a small object-oriented package.

This is a classroom reference implementation, not a complete enterprise deployment.
'@

Write-ProjectFile "day1\employee_training.py" @'
"""Employee training and certification assessment.

Day 1: variables, data types, operators, conditions, loops, validation,
exception handling, counters, accumulators and defensive coding.
"""

import math

MINIMUM_ATTENDANCE = 75.0
MINIMUM_SCORE = 60.0
MAXIMUM_SCORE = 100.0
MAXIMUM_EMPLOYEES = 500


# Validate employee count.
while True:
    try:
        employee_count = int(input("Enter number of employees (1-500): "))
        if 1 <= employee_count <= MAXIMUM_EMPLOYEES:
            break
        print(f"Enter a number between 1 and {MAXIMUM_EMPLOYEES}.")
    except ValueError:
        print("Invalid input. Enter a whole number.")

eligible_count = 0
total_score = 0.0
highest_score = -1.0
highest_employee = ""

# Process employees one at a time.
for employee_number in range(1, employee_count + 1):
    print(f"\n--- Employee {employee_number} ---")

    # Validate employee name.
    while True:
        employee_name = input("Enter employee name: ").strip()
        if employee_name:
            break
        print("Employee name cannot be empty.")

    # Validate attendance.
    while True:
        try:
            attendance = float(input("Enter attendance percentage (0-100): "))
            if math.isfinite(attendance) and 0.0 <= attendance <= 100.0:
                break
            print("Attendance must be a finite number between 0 and 100.")
        except ValueError:
            print("Invalid attendance. Enter a numeric value.")

    # Validate assessment score.
    while True:
        try:
            assessment_score = float(input("Enter assessment score (0-100): "))
            if math.isfinite(assessment_score) and 0.0 <= assessment_score <= MAXIMUM_SCORE:
                break
            print("Score must be a finite number between 0 and 100.")
        except ValueError:
            print("Invalid score. Enter a numeric value.")

    # Check certification eligibility.
    if attendance >= MINIMUM_ATTENDANCE and assessment_score >= MINIMUM_SCORE:
        eligibility_status = "Eligible"
        eligible_count += 1
    else:
        eligibility_status = "Not eligible"

    # Classify performance independently of certification eligibility.
    if assessment_score >= 90:
        performance = "Excellent"
    elif assessment_score >= 75:
        performance = "Good"
    elif assessment_score >= MINIMUM_SCORE:
        performance = "Satisfactory"
    else:
        performance = "Needs improvement"

    total_score += assessment_score

    if assessment_score > highest_score:
        highest_score = assessment_score
        highest_employee = employee_name

    print(f"Employee: {employee_name}")
    print(f"Eligibility: {eligibility_status}")
    print(f"Performance: {performance}")

# Calculate summary metrics.
average_score = total_score / employee_count
ineligible_count = employee_count - eligible_count
eligibility_percentage = (eligible_count / employee_count) * 100.0

print("\n========== TRAINING SUMMARY ==========")
print(f"Total employees: {employee_count}")
print(f"Eligible employees: {eligible_count}")
print(f"Not eligible: {ineligible_count}")
print(f"Average score: {average_score:.2f}")
print(f"Highest score: {highest_score:.2f}")
print(f"Top performer: {highest_employee}")
print(f"Eligibility percentage: {eligibility_percentage:.2f}%")
'@

Write-ProjectFile "day2\employee_training_day2.py" @'
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
'@

Write-ProjectFile "day3\employee_training\__init__.py" @'
"""Employee training management package."""
'@

Write-ProjectFile "day3\employee_training\models.py" @'
"""Employee domain model."""

from dataclasses import dataclass, field
import math


@dataclass
class Employee:
    """Represent an employee participating in training."""

    employee_id: int
    name: str
    department: str
    attendance: float
    score: float
    skills: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate employee attributes after initialization."""
        self.name = self.name.strip()
        self.department = self.department.strip()

        if self.employee_id <= 0:
            raise ValueError("Employee ID must be positive.")
        if not self.name:
            raise ValueError("Employee name is required.")
        if not self.department:
            raise ValueError("Department is required.")
        if not math.isfinite(self.attendance) or not 0 <= self.attendance <= 100:
            raise ValueError("Attendance must be between 0 and 100.")
        if not math.isfinite(self.score) or not 0 <= self.score <= 100:
            raise ValueError("Score must be between 0 and 100.")

        self.skills = [
            skill.strip() for skill in self.skills if skill.strip()
        ]
'@

Write-ProjectFile "day3\employee_training\policies.py" @'
"""Certification policy implementations."""

from abc import ABC, abstractmethod

from employee_training.models import Employee


class CertificationPolicy(ABC):
    """Define a common certification policy interface."""

    @abstractmethod
    def is_eligible(self, employee: Employee) -> bool:
        """Determine employee certification eligibility."""
        raise NotImplementedError


class StandardCertificationPolicy(CertificationPolicy):
    """Apply standard certification requirements."""

    def is_eligible(self, employee: Employee) -> bool:
        return employee.attendance >= 75 and employee.score >= 60


class AdvancedCertificationPolicy(CertificationPolicy):
    """Apply advanced certification requirements."""

    def is_eligible(self, employee: Employee) -> bool:
        return employee.attendance >= 85 and employee.score >= 80
'@

Write-ProjectFile "day3\employee_training\decorators.py" @'
"""Reusable application decorators."""

from collections.abc import Callable
from functools import wraps
import logging
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

logger = logging.getLogger(__name__)


def audit_execution(function: Callable[P, R]) -> Callable[P, R]:
    """Log the execution and failure of an application operation."""

    @wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        logger.info("Starting operation: %s", function.__name__)
        try:
            result = function(*args, **kwargs)
            logger.info("Completed operation: %s", function.__name__)
            return result
        except Exception:
            logger.exception("Operation failed: %s", function.__name__)
            raise

    return wrapper
'@

Write-ProjectFile "day3\employee_training\services.py" @'
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

    def find_eligible_employees(
        self, policy: CertificationPolicy
    ) -> list[Employee]:
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
    def generate_report(
        self, policy: CertificationPolicy
    ) -> TrainingReport:
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
'@

Write-ProjectFile "day3\main.py" @'
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
'@

Write-ProjectFile "day3\tests\test_employee.py" @'
"""Tests for the employee training application."""

import pytest

from employee_training.models import Employee
from employee_training.policies import (
    AdvancedCertificationPolicy,
    StandardCertificationPolicy,
)
from employee_training.services import EmployeeTrainingService


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
'@

# Install only the development tools that are not already available.
Write-Host "`nInstalling/checking development tools in the existing venv..." -ForegroundColor Cyan
& $PythonExe -m pip install --disable-pip-version-check ruff bandit pytest
if ($LASTEXITCODE -ne 0) {
    throw "Package installation failed. Check network access and pip output, then rerun the script."
}

Write-Host "`n=== Setup completed ===" -ForegroundColor Green
Write-Host "Project folder: $ProjectRoot" -ForegroundColor Green
Write-Host "`nNext commands (run from the project folder):" -ForegroundColor Cyan
Write-Host "  Set-Location `"$ProjectRoot`""
Write-Host "  python day1\employee_training.py"
Write-Host "  python day2\employee_training_day2.py"
Write-Host "  python day3\main.py"
Write-Host "  python -m pytest day3\tests -q"
Write-Host "  ruff check ."
Write-Host "  ruff format --check ."
Write-Host "  mypy --strict day3\employee_training day3\main.py"
Write-Host "  bandit -r day3\employee_training"
