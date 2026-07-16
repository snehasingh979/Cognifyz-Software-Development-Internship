import os

FILE_NAME = "students.txt"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()


def add_student():
    name = input("Enter student name: ")
    with open(FILE_NAME, "a") as file:
        file.write(name + "\n")
    print("Student added successfully!")


def view_students():
    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    if not students:
        print("No students found.")
    else:
        print("\nStudent List:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. {student.strip()}")


def update_student():
    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    if not students:
        print("No students found.")
        return

    view_students()

    index = int(input("Enter student number to update: ")) - 1

    if 0 <= index < len(students):
        new_name = input("Enter new student name: ")
        students[index] = new_name + "\n"

        with open(FILE_NAME, "w") as file:
            file.writelines(students)

        print("Student updated successfully!")
    else:
        print("Invalid student number.")


def delete_student():
    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    if not students:
        print("No students found.")
        return

    view_students()

    index = int(input("Enter student number to delete: ")) - 1

    if 0 <= index < len(students):
        removed = students.pop(index)

        with open(FILE_NAME, "w") as file:
            file.writelines(students)

        print(f"{removed.strip()} deleted successfully!")
    else:
        print("Invalid student number.")


while True:
    print("\n===== CRUD WITH FILE HANDLING =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
