def main():
    # Initialize an empty dictionary for the phone book
    phone_book = {}

    # Add some initial entries to the phone book
    phone_book["John"] = "123-456-7890"
    phone_book["Jane"] = "987-654-3210"
    phone_book["Alice"] = "555-123-4567"

    while True:
        print("\nPhone Book Menu:")
        print("1. Look up a phone number")
        print("2. Add a new entry")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            name = input("Enter the name to look up: ")
            if name in phone_book:
                print(f"The phone number for {name} is {phone_book[name]}.")
            else:
                print(f"{name} is not found in the phone book.")

        elif choice == "2":
            name = input("Enter the name: ")
            number = input("Enter the phone number: ")
            phone_book[name] = number
            print(f"Entry for {name} added to the phone book.")

        elif choice == "3":
            print("Exiting the phone book program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
