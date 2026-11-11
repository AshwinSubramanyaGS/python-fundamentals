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
