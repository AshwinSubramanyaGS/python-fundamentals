# Initialize variables
N = int(input("Limit: "))
num = 1
num2 = 4
num3 = 7

# Loop to print the series
while num <= N:
    print(num, end=", " if num2 < N else "\n")
    num, num2, num3 = num2, num3, num + num2 + num3
