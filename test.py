n1 = int(input("Choose any number: "))
n2 = int(input("Choose another number: "))
op = input("Choose an operator: ")

result = 0

if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '*':
    result = n1 * n2
elif op == '/':
    if n2 != 0:
        result = n1 / n2
    else:
        result = "Invalid n2. Try one different from 0"
else:
    result = "Invalid operator"

print(f"result = {result}")

