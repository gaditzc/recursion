def display_menu():
    print("\nChoose an option:")
    print("1. Robot Paths")
    print("2. The Human Pyramid")
    print("3. Parenthesis Validation")
    print("4. Queens Battle")
    print("5. Crossword Generator")
    print("6. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            print("Executing Robot Paths...")
            # Call the Robot Paths function here
        elif choice == '2':
            print("Executing The Human Pyramid...")
            # Call the Human Pyramid function here
        elif choice == '3':
            print("Executing Parenthesis Validation...")
            # Call the Parenthesis Validation function here
        elif choice == '4':
            print("Executing Queens Battle...")
            # Call the Queens Battle function here
        elif choice == '5':
            print("Executing Crossword Generator...")
            # Call the Crossword Generator function here
        elif choice == '6':
            print("Goodbye.")
            break
        else:
            print("Please choose a task number from the list.")


if __name__ == "__main__":
    main()
