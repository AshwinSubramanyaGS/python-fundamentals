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
