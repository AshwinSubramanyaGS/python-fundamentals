import re

import numpy as np
import pandas as pd

EMPLOYEE_PATTERN = re.compile(r"EMP-\d{4}")

EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)


def main():

    # Step 1: Read CSV
    df = pd.read_csv("employees_day5.csv")

    # Step 2: Validate employee IDs and emails
    valid_ids = df["employee_id"].str.fullmatch(
        EMPLOYEE_PATTERN
    )

    valid_emails = df["email"].str.fullmatch(
        EMAIL_PATTERN,
        na=False
    )

    # Step 3: Validate numerical fields
    for column in ["attendance", "score"]:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    valid_numbers = (
        np.isfinite(df["attendance"])
        & np.isfinite(df["score"])
        & df["attendance"].between(0, 100)
        & df["score"].between(0, 100)
    )

    # Step 4: Separate valid and rejected records
    valid_mask = (
        valid_ids
        & valid_emails
        & valid_numbers
    )

    valid_df = df.loc[valid_mask].copy()

    rejected_df = df.loc[~valid_mask].copy()

    # Step 5: Calculate statistics using NumPy
    scores = valid_df["score"].to_numpy()

    if len(scores) == 0:
        print("No valid employee records found.")
        return

    print("Average score:", np.mean(scores))
    print("Highest score:", np.max(scores))
    print("Lowest score:", np.min(scores))

    # Step 6: Filter eligible employees using Pandas
    eligible = valid_df[
        (valid_df["attendance"] >= 75)
        & (valid_df["score"] >= 60)
    ]

    print("\nEligible Employees:")
    print(eligible)

    # Step 7: Department-wise analysis
    print("\nDepartment Performance:")

    print(
        valid_df.groupby("department")["score"].mean()
    )

    # Step 8: Generate reports
    eligible.to_csv(
        "eligible_employees.csv",
        index=False
    )

    rejected_df.to_csv(
        "rejected_employees.csv",
        index=False
    )

    print("\nReports generated successfully.")


if __name__ == "__main__":
    main()
