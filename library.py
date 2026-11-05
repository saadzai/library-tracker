books = {}  

def add_book():
    title = input("Title: ").strip()
    author = input("Author: ").strip()

    if title in books:
        print(f'"{title}" is already in the library.')
    else:
        books[title] = {
            "author": author,
            "available": True
        }
        print(f'Added "{title}".')


def show_menu():
    print("\n=== Library Tracker ===")
    print("1. Add book")
    print("2. List books")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            if not books:
                print("No books in the library.")
            else:
                print("\nBooks in the library:")
                for title, info in books.items():
                    status = "Available" if info["available"] else "Checked out"
                    print(f'"{title}" by {info["author"]} - {status}')
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

