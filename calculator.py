print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus")
choice = int(input('Enter choice(1/2/3/4/5): '))
x = int(input('Enter first number: ' ))
y = int(input('Enter second number: ' ))

if choice == 1:
    def add():
        print (x + y)
    add()

elif choice == 2:
    def subtract():
        print(x - y) 
    subtract()

elif choice == 3:
    def multiply():
        print(x * y)
    multiply()

elif choice == 4:
    def divide():
        print(x / y)
    divide()

elif choice == 5:
    def modulus():
        print(x % y)
    modulus()

else:
    print('invalid choice')





