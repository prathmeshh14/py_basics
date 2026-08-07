import datetime
def calculate_age(birth_date):
    birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
    today = datetime.datetime.now()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birth_date=input("Enter your birth date in the format dd/mm/yyyy: ")
age=calculate_age(birth_date)
print("Your age is:", age)