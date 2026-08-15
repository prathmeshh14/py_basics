expenses = {
    "amount": 0,
    "food": 0,
    "travel": 0,
    "shopping": 0,
    "bills": 0,
    "other": 0
}

def add_expense():
    category = input("Enter the category of expense: ").lower()
    amount = float(input("Enter the amount of expense: "))
    if category in expenses and amount > 0:
        expenses[category] = amount
        expenses["amount"]+=amount
        print(f"Expense of ₹{amount} added to category {category}.")
        view_expenses()
    else:
        print("Please enter a valid category and a positive amount.")
        return

def view_expenses():
    print("\n--- Expense Summary ---")
    for category, amount in expenses.items():
        print(f"{category.capitalize()}: ₹{amount}")
    extra_choice=input("Do you want to perform another action? (y/n): ")
    if extra_choice.lower()=='y':
        main()
    else:
        print("Exiting the program.")
        exit()

def search_expenses():
    category=input("Enter the category to search: ").lower()
    if category in  expenses:
        print(f"Category:.{category}")
        print(f"Amount: ₹{expenses[category]}")

def delete_expenses():
    category=input("Enter the category to search: ").lower()
    if category in  expenses:
        expenses[category]=0
        print(f"Category: {category} , Amount: ₹{expenses[category]}")
    else:
        print("Category not found!!")

def main():
    while True:
        print("1.Add Expenses\n2.View Expenses\n3.Search Expenses\n4.Delete Expenses")
        choice=int(input("Enter the operation you want: "))
        match choice:
            case 1:
                add_expense()
            case 2:
                view_expenses()
            case 3:
                search_expenses()
            case 4:
                delete_expenses()
            case _:
                print("Please enter the valid input :")

if __name__ == "__main__":
    main()