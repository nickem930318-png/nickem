
biblo = {}

def menu():
    print("Menu: ")
    print("1. Add book and author")
    print("2. Modify book and author")
    print("3. Remove book")
    print("4. List all books")
    print("5. Exit")

def selection1():
    book = input("Title: ")
    author = input("Author: ")
    biblo[book] = author
    print(f"The book {book} has been added.")

def selection2():
    bookModify = input("Submit the title of the book to modify: ")
    if bookModify in biblo:
        new_author = input("New Author: ")
        biblo[bookModify] = new_author
        print(f"Information for {bookModify} updated. New author is {new_author}.")
    else:
        print(f"The book with title {bookModify} cannot be found in library.")

def selection3():
    removeBook = input("Please type the title of the book you want to remove: ")
    if removeBook in biblo:
        del biblo[removeBook]
        print(f"{removeBook} has been removed.")
    else:
        print(f"Could not find {removeBook} in the list of books.")

def selection4():
    if biblo:
        for book, author in biblo.items():
                print(f"{book} - {author}")
    else:
        print("There are no books in this library.")

def validation():
    print("Wrong selection, please try again.")


def main():
    while True:
        menu()
        choice = input("Please make a choice between 1-5: ")
        if choice == "1":
            selection1()
        elif choice == "2":
            selection2()
        elif choice == "3":
            selection3()
        elif choice == "4":
            selection4()
        elif choice == "5":
            print("Farewell.")
            break
        else:
            validation()

main()

