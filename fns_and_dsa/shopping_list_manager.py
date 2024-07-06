shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            shopping_list.append(choice)
            print(f"{choice} added successfully")
            pass
        elif choice == '2':
            shopping_list.remove
            print(f"{choice} removed successfully")
            pass
        elif choice == '3':
            shopping_list()
            print(f"{choice} viewed successfully")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
