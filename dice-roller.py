import random

print("\n==== Dice Roller Game ====")

while True:
    roll = input("Roll the dice? (yes/no): ").lower()
    if roll == "yes":
        number = random.randint(1, 6)
        print(f"You rolled a {number}")
    elif roll == "no":
        chance = input("Are you sure? (yes/no)").lower()
        if chance == "no":
            number = random.randint(1, 6)
            print(f"You rolled a {number}")
        else:
            print("Goodbye!")
            break
    else:
        print("Please enter 'yes' or 'no' ")
        break
