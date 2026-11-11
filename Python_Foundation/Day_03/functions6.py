# Combining all argument types for a function
def generate_report(
    employee_name, department, *scores, include_average=True, **metadata
):
    if not scores:
        raise ValueError("At least one score is required.")

    print(f"Employee: {employee_name}")
    print(f"Department: {department}")

    if include_average:
        print(f"Average: {sum(scores) / len(scores):.2f}")

    print("Additional information:", metadata)


generate_report(
    "Rahul",
    "IT",
    80,
    90,
    85,
    include_average=True,
    location="Bengaluru",
    training="Python",
)
