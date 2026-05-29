def check(year):
    if(year%4==0 and year%100!=0) or (year%400==0):
        return 'leap year'
    else:
        return 'not a leap year'
    
year=int(input('Enter a year: '))
result=check(year)
print(f'{year} is a {result}')