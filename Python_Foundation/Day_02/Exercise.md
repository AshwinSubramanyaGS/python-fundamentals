# Part C – Hands-on Exercises

## 13. Participant exercise distribution

Day 2 exercise bank

# 10

Easy

Collection fundamentals

# 10

Medium

Combined operations

# 5

Hard / Tricky

Complexity and edge cases

# 1

Integrated

Business application

# 26

Total exercises, with trainer solution material.

## Easy – 10 exercises

| No. | Exercise                      | Concepts                                |
| --- | ----------------------------- | --------------------------------------- |
| E01 | Employee Name Registry        | List creation and iteration             |
| E02 | Score Access and Slicing      | Indexing, negative indexing and slicing |
| E03 | Employee Attendance Counter   | `count()`, `index()`                    |
| E04 | Employee Name Sorting         | `sort()` and `sorted()`                 |
| E05 | Training Configuration        | Tuple creation and unpacking            |
| E06 | Duplicate Employee ID Removal | Set conversion                          |
| E07 | Common Technical Skills       | Set intersection                        |
| E08 | Employee Profile Dictionary   | Dictionary creation and access          |
| E09 | Optional Employee Attributes  | `get()` and default values              |
| E10 | Passing Score Collection      | List comprehension and filtering        |

## Medium – 10 exercises

| No. | Exercise                               | Concepts                                |
| --- | -------------------------------------- | --------------------------------------- |
| M01 | Employee Record Management             | List of dictionaries, append and update |
| M02 | Employee Skill Frequency Counter       | Dictionary counting pattern             |
| M03 | Duplicate Name Detection               | Sets and ordered deduplication          |
| M04 | Shared Skills Analysis                 | Set union, intersection and difference  |
| M05 | Merge Training Configuration           | Dictionary update and merge             |
| M06 | Department Employee Filtering          | List comprehension                      |
| M07 | Department-wise Performance Statistics | Dictionary and counters                 |
| M08 | Employee ID and Score Mapping          | `zip()` and dictionary comprehension    |
| M09 | Employee Report Generation             | `enumerate()` and formatting            |
| M10 | Multi-criteria Employee Ranking        | `sorted()` and tuple-based sorting      |

## Hard / Tricky – 5 exercises

| No. | Exercise                                   | Challenge                                          |
| --- | ------------------------------------------ | -------------------------------------------------- |
| H01 | Deep Copy Employee Records                 | Shallow copy versus deep copy                      |
| H02 | Safe Employee Record Removal               | Avoid modifying collections during iteration       |
| H03 | Employee Lookup Error Handling             | Missing keys and duplicate identifiers             |
| H04 | Deduplicate Records by Employee ID         | Preserve the latest record without losing ordering |
| H05 | Flatten and Analyze Nested Assessment Data | Nested comprehensions and aggregation              |

## Integrated scenario – 1 exercise

Final practical challenge

H06 – Enterprise Employee Training Analytics System

A company has 100 employees across IT, HR, Finance and Operations departments. Each employee can have multiple skills and assessment records.

Develop an in-memory system that:

1. Stores employee information as a list of dictionaries.
2. Maintains a unique employee lookup using a dictionary.
3. Maintains unique departments and skills using sets.
4. Stores fixed certification criteria in a tuple.
5. Identifies eligible and ineligible employees.
6. Identifies duplicate IDs and duplicate names.
7. Finds common skills across departments.
8. Calculates department-wise average scores.
9. Generates top-five performers.
10. Creates a dictionary of employee IDs and scores.
11. Generates a report using `enumerate()`.
12. Uses comprehensions wherever they improve readability.

Constraints

- No OOPS or class definitions.
- No user-defined functions; these are introduced on Day 3.
- Validate the input records.
- Handle missing optional fields.
- Avoid modifying records during active iteration.
- Use only built-in Python collections and modules for the exercise.
- Run Ruff and Bandit before submission.

Expected outcome: A small but meaningful in-memory employee analytics application, ready to be refactored into a reusable application on Day 3.
