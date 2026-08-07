def odd_even(num):
    if num%2==0:
        return 'Even'
    else:
        return 'Odd'
    
number=int(input('Enter a number: '))
result=odd_even(number)
print(f'The number is: {result}')