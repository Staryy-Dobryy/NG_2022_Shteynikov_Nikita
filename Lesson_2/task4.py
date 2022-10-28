value = int(input("Enter value: "))
result = 1
for i in range(value):
    result *= value - i
print("Result:",result)