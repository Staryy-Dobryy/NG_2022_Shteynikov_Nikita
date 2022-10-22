try:
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))
    operation = input("Enter operation: sum/diff/multiple/divide/power/radical\n")
    print ("Result: ", end="")
    if operation == "sum": 
        print (str(firstNumber + secondNumber))
    elif operation == "diff": 
        print (str(firstNumber - secondNumber))
    elif operation == "multiple": 
        print (str(firstNumber * secondNumber))
    elif operation == "divide":
        if secondNumber == 0: 
            print ("Invalid second number")     #cannot divide by zero
        else: 
            print (str(firstNumber / secondNumber))
    elif operation == "power": 
        print (str(firstNumber ** secondNumber))
    elif operation == "radical":
        if firstNumber < 0: 
            print ("Invalid first number")      #radical expression cannot be negative
        elif secondNumber == 0: 
            print ("Invalid second number")     #root exponent cannot be zero
        else: 
            print (str(firstNumber ** 1/secondNumber))
    else: 
        print ("Invalid operation")
except: 
    print ("Invalid value")