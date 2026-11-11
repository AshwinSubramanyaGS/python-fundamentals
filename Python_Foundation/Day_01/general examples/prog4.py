# Program to impement grading of marks

# Input grade
total_mark = float(input("Enter your grade: "))

# Logic to map the grade to marks
if total_mark >= 90:
    print("A+")
elif total_mark >= 80:
    print("A")
elif total_mark >= 70:
    print("B")
elif total_mark >= 60:
    print("C")
elif total_mark < 60:
    print("F")
else:
    print("Invalid Input")
