
def calculate(result):
    return (result)

while True:
    try:
        print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus")
        choice = int(input('Enter choice (1/2/3/4/5): '))

        if choice <= 0 or choice >= 6:
            print('Please choose 1-5 only')
            continue

        while True:
            try:
                x = float(input("Enter first number: "))
                break
            except ValueError:
                print("Please input a valid number only.")

        while True:
            try:
                y = float(input("Enter second number: "))
                break
            except ValueError:
                print("Please input a valid number only.")

        if choice == 1:
            print(f"Addition => {x} + {y} = {calculate(x + y)}")

        elif choice == 2:
            print(f"Subtraction => {x} - {y} = {calculate(x - y)}")

        elif choice == 3:
            print(f"Multiplication => {x} * {y} = {calculate(x * y)}")

        elif choice == 4:
            if y == 0:
                print(f"Error: Division by '{int(y)}' is not allowed.")
            else:
                print(f"Division => {x} / {y} = {calculate(x / y)}")

        elif choice == 5:
            if y == 0:
                print(f"Error: Modulus by '{int(y)}' is not allowed.")
            else:
                print(f"Modulus => {x} % {y} = {calculate(x % y)}")
        break

    except ValueError:
        print("Error: Please input valid numbers.")
