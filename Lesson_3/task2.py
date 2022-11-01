def tryTransform (value):
    try: return int(value)
    except: return value.lower()

def defineOp(option, string):
    option = tryTransform(option)
    vowels = "aeiouyAEIOUY"
    if option == "sort" or option == 1:
        print(f"Sorted string: {sorted(string)}\n")
    elif option == "count" or option == 2:
        print(f"Count letters: {len(string)}")
    elif option == "vowels" or option == 3:
        for item in string:
            if item in vowels: print(item, end=" ")
        print()
    elif option == "occurring" or option == 4:
        for item in string:
            if item not in vowels: print(item, end=" ") 
        print()
    elif option == "split" or option == 5:
        print(f"Splited string: {string.split(' ')}")
    elif option == "index" or option == 6:
        try:
            index = int(input("Enter index: "))
            print(f"Your word: {string.split(' ')[index]}")
        except:
            print("Invalid value")
    elif option == "show" or option == 7:
        print("Your string: ", string)
    elif option == "exit" or option == 8:
        exit()
    print("====================================")

def main():
    while True:
        string = input("Enter string: ")
        wall = "\n─────────────────────────────────┨"
        print("\nMENU\n─────────────────────────────────┒")
        print("- Sort(1)                        ┃", wall)
        print("- Count(2)                       ┃", wall)
        print("- Only vowels letters(3)         ┃", wall)
        print("- Only occurring letters(4)      ┃", wall)
        print("- Split and show(5)              ┃", wall)
        print("- Word by index(6)               ┃", wall)
        print("- Show string again(7)           ┃", wall)
        print("- Exit(8)                        ┃")
        print("─────────────────────────────────┚")
        defineOp(input("Choose an option: "), string)

main()