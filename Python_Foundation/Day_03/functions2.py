# Function with return values
def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12

employee_details = {"A":12323 ,
                    "B":12388 
                    }

print("-"*30)
#Calculate and print anual salary of each employee
for name,monthly in employee_details.items():
    print(f"|{name:<10}|{monthly:<10}|{calculate_annual_salary(monthly) }|" ,end="\n"+"-"*30 +"\n" )
