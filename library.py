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
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

