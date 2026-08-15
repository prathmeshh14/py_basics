lst=[]
def add_student():
    name=input("Enter student name:")
    rollno=input("Enter student roll number:")
    print("Enter marks of three subjects: \n first subject, second subject, third subject")
    sub1, sub2, sub3 = map(float, input("Enter marks of three subjects separated by space: ").split())
    if 0 <= sub1 <= 100 and 0 <= sub2 <= 100 and 0 <= sub3 <= 100 and len(rollno) == 3:
        student={'name':name,'rollno':rollno,'sub1':sub1,'sub2':sub2,'sub3':sub3}
        lst.append(student)
        print("Student added successfully")
        display_students()
    else:
        print("Invalid marks or roll number. Please enter valid marks (0-100) and a 3-digit roll number.")

def display_grades():
    if not lst:
        print("No students found")
        return
    for student in lst:
        total_marks=student['sub1']+student['sub2']+student['sub3']
        if total_marks>=300:
            grade='A'
        elif total_marks>=250:
            grade='B'
        elif total_marks>=200:
            grade='C'
        else:
            grade='D'

    return grade

def search_student():
    display_students()
    roll_no=input("Enter student roll number to search:")
    if roll_no not in [student['rollno'] for student in lst]:
        print("Student not found.")
        return
    else:
        for student in lst:
            if student['rollno']==roll_no:
                print(f"Name: {student['name']} | Roll Number: {student['rollno']} | Marks: {student['sub1']} | {student['sub2']} | {student['sub3']} | Total: {student['sub1'] + student['sub2'] + student['sub3']} |Grade: {display_grades()}\n")

def display_students():
    print("\nStudent Details:")
    if not lst:
        print("No students found.")
        return 
    else:
        for student in lst:
           print(f"Name: {student['name']} | Roll Number: {student['rollno']} | Marks: {student['sub1']} | {student['sub2']} | {student['sub3']} | Total: {student['sub1'] + student['sub2'] + student['sub3']} |Grade: {display_grades()}\n")
    extra_choice=input("Do you want to perform another action? (y/n): ")
    if extra_choice.lower()=='y':
        main()
    else:
        print("Exiting the program.")
        exit()

def update_student():
    display_students()
    roll_no=input("Enter student roll number to update:")
    if roll_no not in [student["rollno"] for student in lst]:
        print("Student not found.")
        return 
    else:
        for student in lst:
            if student["rollno"]==roll_no:
                print(f"Current details: Name: {student['name']} | Roll Number: {student['rollno']} | Marks: {student['sub1']} | {student['sub2']} | {student['sub3']} | Total: {student['sub1'] + student['sub2'] + student['sub3']} |Grade: {display_grades()}\n")
                name=input("Enter new name (leave blank to keep current): ")
                rollno=input("Enter new roll number (leave blank to keep current): ")
                print("Enter new marks of three subjects (leave blank to keep current): \n first subject, second subject, third subject")
                sub1_input = input("Enter marks of first subject: ")
                sub2_input = input("Enter marks of second subject: ")
                sub3_input = input("Enter marks of third subject: ")

                if name:
                    student["name"] = name
                if rollno:
                    if len(rollno) == 3:
                        student["rollno"] = rollno
                    else:
                        print("Invalid roll number. Keeping current roll number.")
                if sub1_input:
                    sub1 = float(sub1_input)
                    if 0 <= sub1 <= 100:
                        student["sub1"] = sub1
                    else:
                        print("Invalid marks for first subject. Keeping current marks.")
                if sub2_input:
                    sub2 = float(sub2_input)
                    if 0 <= sub2 <= 100:
                        student["sub2"] = sub2
                    else:
                        print("Invalid marks for second subject. Keeping current marks.")
                if sub3_input:
                    sub3 = float(sub3_input)
                    if 0 <= sub3 <= 100:
                        student["sub3"] = sub3
                    else:
                        print("Invalid marks for third subject. Keeping current marks.")

                print("Student details updated successfully.")
                display_students()

def delete_student():
    display_students()
    roll_no=input("Enter student roll number to delete:")
    if roll_no not in [student["rollno"] for student in lst]:
        print("Student not found.")
        return 
    else:
        for student in lst:
            if student["rollno"]==roll_no:
                lst.remove(student)
                print("Student deleted successfully.")
                display_students()
                return

def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice=input("Enter your choice (1-6): ")
        if choice=='1':
            add_student()
        elif choice=='2':
            display_students()
        elif choice=='3':
            search_student()
        elif choice=='4':
            update_student()
        elif choice=='5':
            delete_student()
        elif choice=='6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()