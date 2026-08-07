def calculate(a,b,sign):
    if sign=='+':
        return a+b
    elif sign=='-':
        return a-b
    elif sign=='*':
        return a*b
    elif sign=='/':
        return a/b
    elif sign=='%':
        return a%b
    else:
        return 'Invalid sign'

a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
sign=input('Enter the sign (+, -, *, /, %): ')
result=calculate(a,b,sign)
print(f'The result is: {result}')