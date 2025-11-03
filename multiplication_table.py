number = int(input("Enter the number to get its multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")