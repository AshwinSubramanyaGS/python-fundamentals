# Initializing list

batch1_student_names = ["Quasi","harshita","lakshmi","sanjay","ram"]
batch2_student_names = ["Rahul","Priya","Kiran","Sneha","Arjun"]

""" batch1_student_names.append(batch2_student_names)

print(batch1_student_names)
 """
batch1_student_names.extend(batch2_student_names)
print(batch1_student_names)
batch2_student_names.remove("Kiran")
print(batch2_student_names)
