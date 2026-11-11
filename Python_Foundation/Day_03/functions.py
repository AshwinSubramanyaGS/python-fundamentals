# asd
def check_result(score):
    if score >= 60:
        print("Pass")
    else:
        print("Fail")

student_marks = [90,30,75,88,47,68,59]

for i in range(len(student_marks)):
    print(student_marks[i],end=" : ")
    check_result(student_marks[i])
