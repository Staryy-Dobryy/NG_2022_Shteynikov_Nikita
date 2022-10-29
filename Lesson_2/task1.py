stringArray = list(''.join(sorted(input("Enter string: "))))
arrayOfAmount, arrayOfSymbol = [], []
setStringArray = sorted(set(stringArray))
for i in range(len(setStringArray)):
    arrayOfAmount.append(stringArray.count(setStringArray[i]))
    arrayOfSymbol.append(setStringArray[i])
    print(setStringArray[i], "-", arrayOfAmount[i])
print()
for i in range(len(arrayOfAmount)):
    for j in range(len(arrayOfAmount)):
        if arrayOfAmount[i] > arrayOfAmount[j]:
            tempAmount, tempSymbol = arrayOfAmount[j], arrayOfSymbol[j]
            # tempAmount = arrayOfAmount[j]
            # tempSymbol = arrayOfSymbol[j]
            arrayOfSymbol[j], arrayOfSymbol[i] = arrayOfSymbol[i], tempSymbol
            arrayOfAmount[j], arrayOfAmount[i] = arrayOfAmount[i], tempAmount
for i in range(len(arrayOfAmount)): print(arrayOfAmount[i], "-", arrayOfSymbol[i])