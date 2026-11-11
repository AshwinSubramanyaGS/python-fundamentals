# Class demo 

class Student:
    def __init__(self, name , reg , grade):
        self.name = name
        self.reg = reg
        self.grade = grade

std = Student( "abc",1234,7.2)

print (f"Student name : {std[0].name}")
print (f"Student grade : {std.grade}")