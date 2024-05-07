print("Welcome to the Kings World Calculator")

cal = input("""What operation do you want to use?
1. Add
2. Subtract
3. Divide
4. Multiply
Choose from 1 - 4: """).lower()

def add():
    num = int(input("Enter the First Number you want to Add: "))
    num2 = int(input("Enter the Second number you want to add: "))
    answer = num + num2
    print(answer)

def subtract():
    num = int(input("Enter the First Number you want to Subtract: "))
    num2 = int(input("Enter the Second number you want to Subtract: "))
    answer = num - num2
    print(answer)

def divide():
    num = int(input("Enter the First Number you want to Divide: "))
    num2 = int(input("Enter the Second number you want to Divide: "))
    if num2 != 0:
        answer = num / num2
        print(answer)
    else:
        print("Error: Cannot divide by zero.")

def multiply():
    num = int(input("Enter the First Number you want to Multiply: "))
    num2 = int(input("Enter the Second number you want to multiply: "))
    answer = num * num2
    print(answer)

if cal == '1':
    add()
elif cal == '2':
    subtract()
elif cal == '3':
    divide()
elif cal == '4':
    multiply()
else:
    print("Good bye, and thanks for Using the Kings World Calculator")   