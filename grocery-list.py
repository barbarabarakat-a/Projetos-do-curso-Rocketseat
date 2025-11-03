cart = []

print("     Grocery list      ")

while True:
    print("1. Add your item: ")
    print("2. View your list: ")
    print("3. Remove item: ")
    print("4. Exit: ")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter your item: ")
        quant = int(input("Enter quantity: "))
        cart.append((item, quant))
        print("Item and Quantity added")

    elif choice == "2":
        if not cart:
            print("No items added yet.")

        else:
            for item, quant in cart:
                print (f"{item} {quant}")

    elif choice == "3":
        name = input("Enter the item to delete: ")
        found = False
        for item in cart:
            if item[0] == name:
                cart.remove(item)
                found = True
                print(f"{name} has been removed from the cart.")
                break
        if not found:
            print(f"{name} was not found in you cart.")
    
    elif choice == "4":
        print("Goodbye!")
        break        