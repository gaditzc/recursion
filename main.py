

def is_valid(board, slot, word):
    r, c, length, direction = slot
    if len(word) != length:
        return False

    if direction == 'H':
        for j in range(length):
            if board[r][c + j] not in ('#', word[j]):
                return False
    else:  # Vertical placement
        for i in range(length):
            if board[r + i][c] not in ('#', word[i]):
                return False
    return True


def place_word(board, slot, word):
    r, c, length, direction = slot
    new_board = [row[:] for row in board]  # Copy board to avoid mutation
    if direction == 'H':
        for j in range(length):
            new_board[r][c + j] = word[j]
    else:
        for i in range(length):
            new_board[r + i][c] = word[i]
    return new_board


def solve_crossword(board, slots, words, used_words, idx=0):
    if idx == len(slots):
        return board  # Solved crossword

    slot = slots[idx]
    for i in range(len(words)):  # Using recursion to iterate over words
        if i not in used_words and is_valid(board, slot, words[i]):
            new_board = place_word(board, slot, words[i])
            solution = solve_crossword(new_board, slots, words, used_words | {i}, idx + 1)
            if solution:
                return solution
    return None  # No solution found


def print_board(board):
    for row in board:
        print('|', ' | '.join(row), '|')


def crossword_generator():
    # Input handling (loops allowed for reading input)
    size = int(input("Please enter the dimensions of the crossword grid: "))
    num_slots = int(input("Please enter the number of slots in the crossword: "))

    print("Please enter the details for each slot (Row, Column, Length, Direction):")
    slots = [tuple(input().split()) for _ in range(num_slots)]
    slots = [(int(r), int(c), int(length), direction) for r, c, length, direction in slots]

    num_words = int(input("Please enter the number of words in the dictionary: "))
    while num_words < num_slots:
        print(f"The dictionary must contain at least {num_slots} words. Please enter a valid dictionary size:")
        num_words = int(input())

    print("Please enter the words for the dictionary: ")
    words = [input() for _ in range(num_words)]

    # Initialize the board
    board = [['#' for _ in range(size)] for _ in range(size)]

    # Solve using recursion
    solution = solve_crossword(board, slots, words, set())

    if solution:
        print_board(solution)
    else:
        print("This crossword cannot be solved.")


# Run the crossword generator
crossword_generator()


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


def is_balanced(expression, stack=[]):
    pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
    if not expression:
        return not stack
    char, *rest = expression
    if char in pairs.values():
        return is_balanced(rest, stack + [char])
    elif char in pairs.keys():
        return stack and stack[-1] == pairs[char] and is_balanced(rest, stack[:-1])
    return is_balanced(rest, stack)


def parenthesis_validation():
    expression = list(input("Please enter a term for validation: "))
    if is_balanced(expression):
        print("The parentheses are balanced correctly.")
    else:
        print("The parentheses are not balanced correctly.")


def solve_queens(i, j, board, cols, colors, sol):
    if i == len(board):
        return sol
    if j == len(board):
        return None
    if j not in cols and board[i][j] not in colors and (i - 1, j - 1) not in sol and (i - 1, j + 1) not in sol:
        sol_ = solve_queens(i + 1, 0, board, cols | {j}, colors | {board[i][j]}, sol | {(i, j)})
        if sol_:
            return sol_
    return solve_queens(i, j + 1, board, cols, colors, sol)


def queens_battle():
    size = int(input("Please enter the board size: "))
    print(f"Please enter the {size}x{size} board:")

    board = [list(input().strip()) for _ in range(size)]
    solution = solve_queens(0, 0, board, set(), set(), set())
    if solution:
        output_board = [['*' for _ in range(size)] for _ in range(size)]
        for r, c in solution:
            output_board[r][c] = 'X'
        print("Solution:")
        for row in output_board:
            print(" ".join(row))
    else:
        print("No valid solution found.")


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
            queens_battle()
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