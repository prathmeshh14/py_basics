try:
    with open("String&file/sample.txt",'r')as f:
        data=f.read()

    words=data.split()
    print("the number of words in the file is:",len(words))

except FileNotFoundError:
    print("file not found") 