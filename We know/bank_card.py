numCard = list(input("Enter number: "))
firstTwo = numCard[0] + numCard[1]
lenght = len(numCard)
if firstTwo == "34" and lenght == 15 or firstTwo == "37" and lenght == 15:
    print("AMEX")
elif firstTwo == "51" and lenght == 16 or firstTwo == "52" and lenght == 16 or firstTwo == "53" and lenght == 16 or firstTwo == "54" and lenght == 16 or firstTwo == "55" and lenght == 16:
    print("MASTERCARD")
elif numCard[0] == "4" and lenght == 13 or numCard[0] == "4" and lenght == 16:
    print("VISA")
else:
    print("INVALID")