def sum(a, b):
    print (str(a + b))

def diff(a, b):
    print (str(a - b))

def multiple(a, b):
    print (str(a * b))

def divide(a, b):
    if b == 0: 
        print ("Invalid second number")
    else:
        print (str(a / b))

def power(a, b): 
    print (str(a ** b))

def radical(a, b):
    if a < 0: 
        print ("Invalid first number")
    elif b == 0: 
        print ("Invalid second number")
    else: 
        print (str(a ** (1/b)))

def askNumber(value):
    try: 
        return int(input(value))
    except:
        print("Invalid value")
        quit()

def calculate(firstNumber, secondNumber):
    operation = input("Enter operation: sum(1) |diff(2) |multiple(3) |divide(4) |power(5) |radical(6)\n")
    print ("Result: ", end="")
    if operation == '1': 
        sum(firstNumber, secondNumber)
    elif operation == '2': 
        diff(firstNumber, secondNumber)
    elif operation == '3': 
        multiple(firstNumber, secondNumber)
    elif operation == '4':
        divide(firstNumber, secondNumber)
    elif operation == '5': 
        power(firstNumber, secondNumber)
    elif operation == '6':
        radical(firstNumber, secondNumber)
    else: 
        print ("Invalid operation")

def Calculator():
    firstNumber = askNumber("Enter first number: ")
    secondNumber = askNumber("Enter second number: ")
    calculate(firstNumber, secondNumber)

Calculator()