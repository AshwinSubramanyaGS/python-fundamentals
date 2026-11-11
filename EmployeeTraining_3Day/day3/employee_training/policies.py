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
