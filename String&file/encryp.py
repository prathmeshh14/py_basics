text=input("Enter the text to encrypt: ")
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""

for char in text:
    if char in alphabet:
        index = (alphabet.index(char) + shift) % 26
        result += alphabet[index]
    else:
        result += char
print(f"encrypted to {text}: {result}")