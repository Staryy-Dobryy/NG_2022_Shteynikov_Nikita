def sum(firstNumber, secondNumber):
    print (str(firstNumber + secondNumber))

def diff(firstNumber, secondNumber):
    print (str(firstNumber - secondNumber))

def multiple(firstNumber, secondNumber):
    print (str(firstNumber * secondNumber))

def divide(firstNumber, secondNumber):
    if secondNumber == 0: 
        print ("Invalid second number")
    else:
        print (str(firstNumber / secondNumber))

def power(firstNumber, secondNumber): 
    print (str(firstNumber ** secondNumber))

def radical(firstNumber, secondNumber):
    if firstNumber < 0: 
        print ("Invalid first number")
    elif secondNumber == 0: 
        print ("Invalid second number")
    else: 
        print (str(firstNumber ** (1/secondNumber)))

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