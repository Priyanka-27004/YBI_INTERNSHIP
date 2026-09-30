books = []

while True:
    print("\n==============================")
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "name": book_name,
            "author": author,
            "issued": False
        }

        books.append(book)

        print("Book added successfully!")

    # View Books
    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\n========== BOOK LIST ==========")

            for book in books:
                print("Book ID:", book["id"])
                print("Book Name:", book["name"])
                print("Author:", book["author"])

                if book["issued"]:
                    print("Status: Issued")
                else:
                    print("Status: Available")

                print("------------------------------")

    # Search Book
    elif choice == "3":
        search = input("Enter Book ID or Book Name: ")

        found = False

        for book in books:
            if book["id"] == search or book["name"].lower() == search.lower():
                print("\nBook Found!")
                print("Book ID:", book["id"])
                print("Book Name:", book["name"])
                print("Author:", book["author"])

                if book["issued"]:
                    print("Status: Issued")
                else:
                    print("Status: Available")

                found = True

        if not found:
            print("Book not found.")

    # Issue Book
    elif choice == "4":
        book_id = input("Enter Book ID to issue: ")

        found = False

        for book in books:
            if book["id"] == book_id:
                found = True

                if book["issued"]:
                    print("Book is already issued.")
                else:
                    book["issued"] = True
                    print("Book issued successfully!")

        if not found:
            print("Book not found.")

    # Return Book
    elif choice == "5":
        book_id = input("Enter Book ID to return: ")

        found = False

        for book in books:
            if book["id"] == book_id:
                found = True

                if book["issued"]:
                    book["issued"] = False
                    print("Book returned successfully!")
                else:
                    print("Book was not issued.")

        if not found:
            print("Book not found.")

    # Delete Book
    elif choice == "6":
        book_id = input("Enter Book ID to delete: ")

        found = False

        for book in books:
            if book["id"] == book_id:
                books.remove(book)
                print("Book deleted successfully!")
                found = True
                break

        if not found:
            print("Book not found.")

    # Exit
    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
