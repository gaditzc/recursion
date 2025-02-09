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


def pyramid_weight(row, col, pyramid):
    if row < 0 or col < 0 or col > row:
        return 0
    if row == 0:
        return pyramid[0][0]
    left_parent = pyramid_weight(row - 1, col - 1, pyramid) if col > 0 else 0
    right_parent = pyramid_weight(row - 1, col, pyramid) if col < row else 0
    return (left_parent / 2) + (right_parent / 2) + pyramid[row][col]


def human_pyramid():
    print("Please enter the weights of the cheerleaders:")
    pyramid = []
    for i in range(1, 6):
        row = list(map(float, input().split()))
        if any(w < 0 for w in row):
            print("Negative weights are not supported.")
            return
        pyramid.append(row)

    print("The total weight on each cheerleader is:")
    for i in range(5):
        print(" ".join(f"{pyramid_weight(i, j, pyramid):.2f}" for j in range(i + 1)))


def is_balanced_helper(chars, stack, index):
    if index == len(chars):
        return not stack

    char = chars[index]
    opening = "({[<"
    closing = ")}]>"
    pairs = {')': '(', ']': '[', '}': '{', '>': '<'}

    if char in opening:
        stack.append(char)
    elif char in closing:
        if not stack or stack[-1] != pairs[char]:
            return False
        stack.pop()

    return is_balanced_helper(chars, stack, index + 1)


def parenthesis_validation():
    print("Please enter a term for validation:")
    chars = list(input())
    if is_balanced_helper(chars, [], 0):
        print("The parentheses are balanced correctly.")
    else:
        print("The parentheses are not balanced correctly.")


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
            human_pyramid()
        elif choice == '3':
            print("Executing Parenthesis Validation...")
            parenthesis_validation()
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
