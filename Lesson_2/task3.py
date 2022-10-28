value = int(input("Enter value: "))
for i in range(value):
    for j in range(value - i):
        print(value - i - j, end=" ")
    print()