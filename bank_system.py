print("------ Welcome to Python Bank ------")

balance = 0

while True:

    print("\n1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Money deposited successfully!")
        print("Current Balance:", balance)

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))

        if amount > balance:
            print("Insufficient balance!")
        else:
            balance = balance - amount
            print("Money withdrawn successfully!")
            print("Remaining Balance:", balance)

    elif choice == "3":
        print("Your Current Balance is:", balance)

    elif choice == "4":
        print("Thank you for using Python Bank")
        break

    else:
        print("Invalid choice! Try again.")