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
    operation = input("Enter operation: sum(+) |diff(-) |multiple(*) |divide(/) |power(**) |radical(√)\n")
    print ("Result: ", end="")
    match operation:
        case '+': 
            sum(firstNumber, secondNumber)
        case '-': 
            diff(firstNumber, secondNumber)
        case '*': 
            multiple(firstNumber, secondNumber)
        case '/':
            divide(firstNumber, secondNumber)
        case '^': 
            power(firstNumber, secondNumber)
        case '√':
            radical(firstNumber, secondNumber)
        case _: 
            print ("Invalid operation")

def Calculator():
    firstNumber = askNumber("Enter first number: ")
    secondNumber = askNumber("Enter second number: ")
    calculate(firstNumber, secondNumber)

Calculator()