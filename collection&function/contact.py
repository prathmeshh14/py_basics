import re
from unittest import case
lst=[]
def add_contact():
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    while True:
        name=input("Name:")
        phone=input("Phone:")
        email=input("Email:")
        if len(phone)==10 and re.match(email_pattern,email) and phone.isdigit():
            contact = {"name": name, "phone": phone, "email": email}
            lst.append(contact)
            print("Contact added successfully.")
            display_contacts()
            break
        else:
            print("\n❌ Invalid Input! Phone must be exactly 10 digits. Email must be valid (e.g., name@domain.com).")
            print("Please try again.\n")
        task=input("Do you want to add another contact? (y/n): ")
        if task.lower()!="y":
            return False
        else:
            return True

def display_contacts():
    print("Contacts:")
    for i,contact in enumerate(lst,start=1):
        print(f"{i} - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    ask_to_continue()

def edit_contact():
    display_contacts()
    contact_number=int(input("Enter the contact number to edit: "))
    if 1<=contact_number<=len(lst):
        contact = lst[contact_number - 1]
        print(f"Editing contact: {contact['name']}")
        new_name = input("Enter new name (or press Enter to keep current): ").strip()
        new_phone = input("Enter new phone (or press Enter to keep current): ").strip()
        new_email = input("Enter new email (or press Enter to keep current): ").strip()

        if new_name:
            contact['name'] = new_name
        if new_phone:
            contact['phone'] = new_phone
        if new_email:
            contact['email'] = new_email

        print("Contact updated successfully.")
    else:
        print("Invalid contact number.")

def delete_contact():
    display_contacts()
    contact_number=int(input("Enter the contact number to delete: "))
    if 1<=contact_number<=len(lst):
        deleted_contact = lst.pop(contact_number - 1)
        print(f"Contact '{deleted_contact['name']}' deleted.")
    else:
        print("Invalid contact number.")

def search_contact():
    query=input("Enter the name or email to search: ").lower().strip()
    if not query:
        print("Search query cannot be empty.")
        return
    results=[]
    for contact in lst:
        if query in contact['name'].lower() or query in contact['email'].lower() or query in contact['phone']:
            results.append(contact)

    print("\nSearch Results:")
    if results:
        for i,contact in enumerate(results,start=1):
            print(f"{i} - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found matching the search criteria.")

def ask_to_continue():
    while True:
        extra = input("Do you want to perform another action? (y/n): ").strip().lower()
        if extra == "y":
            return True
        elif extra == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

while True:
    try:
        print("\nContact Management Menu:"
            "\n1. Add contact"
            "\n2. Display contacts"
            "\n3. Edit contact"
            "\n4. Delete contact"
            "\n5. Search contact")
        choice = input("Enter your choice : ").strip()
        match choice:
            case "1":
                add_contact()
            case "2":
                display_contacts()
            case "3":
                edit_contact()
            case "4":
                delete_contact()
            case "5":
                search_contact()
            case _:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
                continue 
                
        if not ask_to_continue():
            print("Goodbye!")
            break
    except Exception as e:
        print(f"An error occurred: {e}")