## Level 2 – Medium exercises

Focus: combined conditions, nested logic, loop control, validation and business rules.

| No. | Exercise                       | Requirements                                                                      |
| --- | ------------------------------ | --------------------------------------------------------------------------------- |
| M01 | Progressive Electricity Bill   | Apply three unit-based tariff slabs and calculate the cumulative bill.            |
| M02 | Employee Overtime Calculator   | Calculate basic and overtime pay using a 40-hour workweek and 1.5x overtime rate. |
| M03 | Leap Year Detector             | Identify leap years using Gregorian calendar rules.                               |
| M04 | Assessment Grade Calculator    | Accept a score, validate it and assign the correct grade.                         |
| M05 | Secure Login Attempt Simulator | Allow three attempts, stop immediately on success and report exhausted attempts.  |
| M06 | ATM Withdrawal Simulator       | Check balance, withdrawal validity, denomination and available funds.             |
| M07 | Divisibility Analyzer          | Display numbers divisible by 3, 5 or both within a user-supplied range.           |
| M08 | Prime Number Detector          | Determine whether a positive integer greater than one is prime.                   |
| M09 | Assessment Analytics           | Calculate average score, number of passes, fails and pass percentage.             |
| M10 | Menu-Driven Calculator         | Support addition, subtraction, multiplication and division until the user exits.  |


## Level 3 – Hard / Tricky exercises

Advanced problem solving

These five questions should be treated as analytical coding challenges rather than straightforward syntax exercises.

| No. | Exercise                       | Requirements                                                                                      |
| --- | ------------------------------ | ------------------------------------------------------------------------------------------------- |
| H01 | Second Largest Distinct Number | Find the second-largest distinct value among three inputs, handling duplicates.                   |
| H02 | Number Guessing Challenge      | Generate a random number and give the user a limited number of attempts, with higher/lower hints. |
| H03 | Reverse an Integer             | Reverse the digits mathematically without converting the number to a string.                      |
| H04 | Sum of Digits                  | Calculate the digit sum of a positive or negative integer without string conversion.              |
| H05 | Prime Number Series            | Generate every prime number up to N using nested loops and an optimized divisor boundary.         |

## Level 4 – Integrated scenario challenge

H06 – Business scenario

Employee Training Certification and Performance Reporting

Business context

A company is conducting a technical training programme for 50 employees. HR wants to identify certification eligibility and generate a performance report.

Functional requirements

1. Accept the number of employees (maximum 500).
2. Capture employee name, attendance and assessment score.
3. Validate names and numeric ranges.
4. Require at least 75% attendance and 60 assessment marks for certification.
5. Classify performance into four grades.
6. Calculate average assessment score.
7. Identify the highest-performing employee.
8. Identify the lowest-performing employee.
9. Calculate eligibility percentage.
10. Count employees in each performance category.

Technical constraints

- Use variables, operators, conditions, loops and exception handling.
- Do not use lists, dictionaries, functions, classes or external libraries.
- Reject invalid attendance and marks rather than silently skipping them.
- Test boundary values and invalid inputs.
- Run Ruff and Bandit before submission.

Expected business output

```
EMPLOYEE TRAINING REPORT
------------------------
Total participants       : 50
Eligible participants    : 38
Not eligible             : 12
Excellent                : 10
Good                     : 15
Average                  : 18
Needs Improvement        : 7
Average assessment      : 74.65
Certification rate      : 76.00%
Top performer            : Employee 024
```
