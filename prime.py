def prime(num):
    if num <2:
        return 'Not a prime number'
    for i in range(2,num):
        if num%i==0:
            return 'Not a prime number'
    return 'Prime number'

number=int(input('Enter a number: '))
result=prime(number)
print(f'{number} is a {result}')



