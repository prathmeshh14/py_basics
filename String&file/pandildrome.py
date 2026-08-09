with open("String&file/sample.txt", 'r') as f:
    data = f.read()

lst=[x for x in data.split() if x==x[::-1]]
print(f"Palindrome words in the file are: {lst}")