default = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
ROT13 = list("NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
text = list(input("Enter text for decoding: "))
print("\nDeciphered text:")
for item in text:
    if item in ROT13:
        index = ROT13.index(item)
        item = default[index]
    print(item, end="")