def _sort(string):
    print(f"Sorted string: {sorted(string)}\n")

def _count(string):
    print(f"Count letters: {len(string)}")

def _vowels(string):
    vowels = "aeiouyAEIOUY"
    for item in string:
        if item in vowels: print(item, end=" ")
    print()

def _occurring(string):
    vowels = "aeiouyAEIOUY"
    for item in string:
        if item not in vowels: print(item, end=" ") 
    print()

def _split(string):
    print(f"Splited string: {string.split(' ')}")

def _index(string):
    try:
        index = int(input("Enter index: "))
        print(f"Your word: {string.split(' ')[index]}")
    except:
        print("Invalid value")

def _show(string):
    print("Your string: ", string)


def tryTransform (value):
    try: return int(value)
    except: return value.lower()

def defineOp(option, string):
    option = tryTransform(option)
    if option == "sort" or option == 1:
        _sort(string)
    elif option == "count" or option == 2:
        _count(string)
    elif option == "vowels" or option == 3:
        _vowels(string)
    elif option == "occurring" or option == 4:
        _occurring(string)
    elif option == "split" or option == 5:
        _split(string)
    elif option == "index" or option == 6:
        _index(string)
    elif option == "show" or option == 7:
        _show(string)
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