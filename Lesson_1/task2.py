try:
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))
    operation = input("Enter operation: sum/diff/multiple/divide/power/radical\n")
    if operation == "sum":
        print ("Result:" + str(firstNumber + secondNumber))
    elif operation == "diff":
        print ("Result:" + str(firstNumber - secondNumber))
    elif operation == "multiple":
        print ("Result:" + str(firstNumber * secondNumber))
    elif operation == "divide":
        if secondNumber == 0:
            print ("Invalid second number")     #cannot divide by zero
        else:
            print ("Result:" + str(firstNumber / secondNumber))
    elif operation == "power":
        print ("Result:" + str(firstNumber ** secondNumber))
    elif operation == "radical":
        if firstNumber < 0:
            print ("Invalid first number")      #radical expression cannot be negative
        elif secondNumber == 0:
            print ("Invalid second number")     #root exponent cannot be zero
        else:
            print ("Result: " + str(firstNumber ** 1/secondNumber))
    else:
        print ("Invalid operation")
except:
    print ("Invalid value")