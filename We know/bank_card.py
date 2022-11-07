numCard = list(input("Enter number: "))
amexNumber = ['34', '37']
mastercardNumber = ['51', '52', '53', '54', '55']
firstTwo = numCard[0] + numCard[1]
lenght = len(numCard)
if firstTwo in amexNumber and lenght == 15:
    print("AMEX")
elif firstTwo in mastercardNumber and lenght == 16:
    print("MASTERCARD")
elif numCard[0] == "4" and lenght == 13 or numCard[0] == "4" and lenght == 16:
    print("VISA")
else:
    print("INVALID")