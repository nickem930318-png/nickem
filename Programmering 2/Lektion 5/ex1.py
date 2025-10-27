def main():
    students = {}

    while True:
        print("Menu: ")
        print("1. Add new student.")
        print("2. Remove existing student.")
        print("3. List all existing students.")
        print("4. Exit.")

        choice = input("Please make a choice between 1-4: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            students[name] = age
            print(f"The student {name} has been added.")
        elif choice == "2":
            removeStudent = input("Please type the name of the student you want to remove: ")
            if removeStudent in students:
                del students[name]
                print(f"Student {name} has been removed.")
            else:
                print(f"Could not find {name} in the list of students.")

        elif choice == "3":
            if students:
                for name, age in students.items():
                    print(f"{name} - {age} years old.")
            else:
                print("There are no students in this class.")
        elif choice == "4":
            break
        else:
            print("Wrong selection, please try again.")

main()