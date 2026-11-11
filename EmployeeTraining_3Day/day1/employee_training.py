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
