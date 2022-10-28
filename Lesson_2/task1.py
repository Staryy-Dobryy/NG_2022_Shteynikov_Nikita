stringArray = list(''.join(sorted(input("Enter string: "))))
arrayOfAmount, arrayOfSymbol = [], []
for index in range(len(stringArray)):
    amount = 0
    temp = stringArray[index]
    if temp != stringArray[index - 1]:
        for ID in range(len(stringArray)):  
            if stringArray[ID] == temp: amount += 1
            if ID + 1 == len(stringArray):
                print(stringArray[index], "-", amount)
                arrayOfSymbol.append(stringArray[index])
                arrayOfAmount.append(amount)
print()
temp = 0
for i in range(len(arrayOfAmount)):
    for j in range(len(arrayOfAmount)):
        if arrayOfAmount[i] > arrayOfAmount[j]:
            tempAmount, tempSymbol = arrayOfAmount[j], arrayOfSymbol[j]
            # tempAmount = arrayOfAmount[j]
            # tempSymbol = arrayOfSymbol[j]
            arrayOfSymbol[j], arrayOfSymbol[i] = arrayOfSymbol[i], tempSymbol
            arrayOfAmount[j], arrayOfAmount[i] = arrayOfAmount[i], tempAmount
for i in range(len(arrayOfAmount)): print(arrayOfAmount[i], "-", arrayOfSymbol[i])