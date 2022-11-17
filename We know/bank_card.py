def validCheck(number):
    index = len(number) - 2
    validSum = 0
    while (index >= -1):
        temp = int(number[index]) * 2
        validSum += int(number[index + 1])
        if index == -1: break
        for item in str(temp): validSum += int(item)
        index -= 2
    if str(validSum)[-1] == "0": print("VALID NUMBER")
    else: print("INVALID NUMBER")

def checkCard(numCard):
    amexNumber = ['34', '37']
    mastercardNumber = ['51', '52', '53', '54', '55']
    firstTwo = numCard[0] + numCard[1]
    lenght = len(numCard)
    if firstTwo in amexNumber and lenght == 15:
        print("AMEX")
        validCheck(numCard)
    elif firstTwo in mastercardNumber and lenght == 16:
        print("MASTERCARD")
        validCheck(numCard)
    elif numCard[0] == "4" and lenght == 13 or numCard[0] == "4" and lenght == 16:
        print("VISA")
        validCheck(numCard)
    else:
        print("INVALID")

checkCard(input("Enter number: "))
    