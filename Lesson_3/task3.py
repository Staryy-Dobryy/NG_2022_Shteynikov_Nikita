def count(stringArray, lenght):
    if lenght == 0: quit()
    amount = stringArray.count(stringArray[lenght - 1])
    print(stringArray[lenght - 1], "-", amount)
    lenght -= amount
    return count(stringArray, lenght)

string = sorted(input("Enter string: "), reverse = True)
count(string, len(string))