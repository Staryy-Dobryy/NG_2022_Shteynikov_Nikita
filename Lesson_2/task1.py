stringArray = list(''.join(sorted(input("Enter string: "))))
dct = {}
for index in range(len(stringArray)):
    dct[stringArray[index]] = stringArray.count(stringArray[index])
sortedDctNum = dict(sorted(dct.items(), key = lambda x: x[1], reverse=True))
print (dct)
print (sortedDctNum)