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
