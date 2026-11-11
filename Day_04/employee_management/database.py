import sqlite3

from contextlib import closing
from pathlib import Path


DATABASE_PATH = Path("training.db")


def get_connection():

    connection = sqlite3.connect(DATABASE_PATH)

    connection.row_factory = sqlite3.Row

    connection.execute("PRAGMA foreign_keys = ON")

    return connection


def initialize_database():

    with closing(get_connection()) as connection:

        with connection:

            connection.execute("""
                CREATE TABLE IF NOT EXISTS employees (

                    employee_id INTEGER PRIMARY KEY,

                    name TEXT NOT NULL,

                    department TEXT NOT NULL,

                    attendance REAL NOT NULL
                        CHECK(attendance BETWEEN 0 AND 100),

                    score REAL NOT NULL
                        CHECK(score BETWEEN 0 AND 100),

                    created_at TEXT NOT NULL
                        DEFAULT CURRENT_TIMESTAMP
                )
            """)

            connection.execute("""
                CREATE TABLE IF NOT EXISTS courses (

                    course_id INTEGER PRIMARY KEY,

                    course_name TEXT NOT NULL UNIQUE
                )
            """)

            connection.execute("""
                CREATE TABLE IF NOT EXISTS enrollments (

                    enrollment_id INTEGER PRIMARY KEY,

                    employee_id INTEGER NOT NULL,

                    course_id INTEGER NOT NULL,

                    score REAL NOT NULL
                        CHECK(score BETWEEN 0 AND 100),

                    FOREIGN KEY(employee_id)
                        REFERENCES employees(employee_id),

                    FOREIGN KEY(course_id)
                        REFERENCES courses(course_id),

                    UNIQUE(employee_id, course_id)
                )
            """)


def bulk_insert_employees(employees):

    with closing(get_connection()) as connection:

        with connection:

            connection.executemany("""
                INSERT INTO employees
                (
                    employee_id,
                    name,
                    department,
                    attendance,
                    score
                )
                VALUES (?, ?, ?, ?, ?)
            """, [
                (
                    emp["employee_id"],
                    emp["name"],
                    emp["department"],
                    emp["attendance"],
                    emp["score"]
                )
                for emp in employees
            ])


def create_course(course_name):

    with closing(get_connection()) as connection:

        with connection:

            connection.execute("""
                INSERT INTO courses (course_name)
                VALUES (?)
                ON CONFLICT(course_name) DO NOTHING
            """, (course_name,))


def enroll_employee(employee_id, course_name, score):

    with closing(get_connection()) as connection:

        with connection:

            connection.execute("""
                INSERT INTO enrollments
                (employee_id, course_id, score)

                SELECT ?, course_id, ?
                FROM courses
                WHERE course_name = ?
            """, (employee_id, score, course_name))


# READ operation

def get_all_employees():

    with closing(get_connection()) as connection:

        return connection.execute("""
            SELECT *
            FROM employees
            ORDER BY employee_id
        """).fetchall()


# READ single employee

def get_employee(employee_id):

    with closing(get_connection()) as connection:

        return connection.execute("""
            SELECT *
            FROM employees
            WHERE employee_id = ?
        """, (employee_id,)).fetchone()


# UPDATE operation

def update_employee_score(employee_id, new_score):

    with closing(get_connection()) as connection:

        with connection:

            cursor = connection.execute("""
                UPDATE employees
                SET score = ?
                WHERE employee_id = ?
            """, (new_score, employee_id))

            return cursor.rowcount


# DELETE operation

def delete_employee(employee_id):

    with closing(get_connection()) as connection:

        with connection:

            cursor = connection.execute("""
                DELETE FROM employees
                WHERE employee_id = ?
            """, (employee_id,))

            return cursor.rowcount


# SQL GROUP BY and aggregate functions

def department_report():

    with closing(get_connection()) as connection:

        return connection.execute("""
            SELECT

                department,

                COUNT(*) AS employee_count,

                AVG(score) AS average_score,

                MAX(score) AS highest_score

            FROM employees

            GROUP BY department

            ORDER BY average_score DESC
        """).fetchall()


# SQL JOIN

def course_report():

    with closing(get_connection()) as connection:

        return connection.execute("""
            SELECT

                e.employee_id,

                e.name,

                c.course_name,

                en.score

            FROM employees e

            JOIN enrollments en
                ON e.employee_id = en.employee_id

            JOIN courses c
                ON en.course_id = c.course_id

            ORDER BY e.employee_id
        """).fetchall()


# Transaction demonstration

def transfer_score_transaction():

    with closing(get_connection()) as connection:

        try:

            with connection:

                connection.execute("BEGIN")

                connection.execute("""
                    UPDATE employees
                    SET score = 95
                    WHERE employee_id = 101
                """)

                # Deliberately invalid score.
                # CHECK constraint will reject this operation.

                connection.execute("""
                    UPDATE employees
                    SET score = 150
                    WHERE employee_id = 102
                """)

        except sqlite3.IntegrityError:

            print("Transaction failed. Changes rolled back.")