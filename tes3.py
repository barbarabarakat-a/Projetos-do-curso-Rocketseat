print("==== Movie Ticket Price Calculator ====")

age = int(input("Enter your age: "))
price = "None"
message = "None"


if age <= 5:
    price = 0
    message = "You do not need to pay"
elif age > 5 and age < 62:
    student = input("Are you a student? (yes/no) ").lower()
    if student == "yes":
        price = 7
        message = f"You need to pay: {price}"
    else:
        price = 14
        message = f"You need to pay {price}"
elif age >= 62:
    price = 6
    message = f"Senior discount. You need to pay {price}"

print(message)