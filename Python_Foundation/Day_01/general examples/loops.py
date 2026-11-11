number = int(input("Enter a number betweeen 2-20: "))

for i in range(1, 11, 2):
    print(f"{number} X {i} = {number * i}", end="|\n")
