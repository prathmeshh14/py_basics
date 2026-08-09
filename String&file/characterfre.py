with open ("String&file/sample.txt",'r')as f:
    data=f.read()
data=data.split()
freq={x: data.count(x) for x in set(data)}
print(f"the frequency of each word in the file is: {freq}")