import math

while True:
    # 1. Show menu
    print("Welcome to CLI calculator!")
    print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Square root 6.Modulus 7.Floor division 8.Exit")

    choice = input("Enter choice (1-8): ").strip()

    # 2. Exit
    if choice == "8":
        print("Exiting...")
        break

    # 3. Invalid choice
    if choice not in ["1","2","3","4","5","6","7"]:
        print("Invalid choice, try again.\n")
        continue

    # 4. Single-number operation (square root)
    if choice == "5":
        try:
            num = float(input("Enter number: "))
            result = math.sqrt(num)
        except ValueError:
            print("Invalid number!")
            continue
        except:
            print("Cannot take square root of negative number!")
            continue

    # 5. Two-number operations
    else:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid numbers!")
            continue

        if choice == "1":
            result = a + b
        elif choice == "2":
            result = a - b
        elif choice == "3":
            result = a * b
        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero!")
                continue
            result = a / b
        elif choice == "6":
            if b == 0:
                print("Cannot modulus by zero!")
                continue
            result = a % b
        elif choice == "7":
            if b == 0:
                print("Cannot floor divide by zero!")
                continue
            result = a // b

    # 6. Print result
    print("Result:", result, "\n")
