

while True:
    print("           MENU       ")
    print("1. Contar de 1 a 10")
    print("2. Contar de 10 a 1")
    print("3. Sair")
    
    choice = (input("Enter the number: "))
    
    if choice == "1":
        for i in range(1, 11):
            print(f"{i}")

    elif choice == "2":
        for i in range(10, 0, -1):
            print(f"{i}")

    elif choice == "3":
        print("Saindo...")
        break