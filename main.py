def display_menu():
    print("\nChoose an option:")
    print("1. Robot Paths")
    print("2. The Human Pyramid")
    print("3. Parenthesis Validation")
    print("4. Queens Battle")
    print("5. Crossword Generator")
    print("6. Exit")


def robot_paths(x, y):
    if x < 0 or y < 0:
        return 0
    if x == 0 and y == 0:
        return 1
    return robot_paths(x - 1, y) + robot_paths(x, y - 1)


def main():
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            print("Executing Robot Paths...")
            x, y = map(int, input("Please enter the coordinates of the robot (column, row): ").split())
            result = robot_paths(x, y)
            print(f"The total number of paths the robot can take to reach home is: {result}")
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
