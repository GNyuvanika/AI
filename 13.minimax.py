# Function to check if the current player has won
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != '-' for i in range(3) for j in range(3))

# Function to evaluate the score of the current board
def evaluate(board):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0
    else:
        return None

# Minimax algorithm
def minimax(board, depth, maximizing_player):
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = '-'  # Undo the move
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = '-'  # Undo the move
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the optimal move using the Minimax algorithm
def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = '-'  # Undo the move

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Function to print the current state of the board
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Main function
def main():
    # Initial empty tic-tac-toe board
    board = [['-' for _ in range(3)] for _ in range(3)]

    print("Initial Board:")
    print_board(board)

    for _ in range(4):  # Play four moves
        # Player X's move
        x, y = map(int, input("Enter the coordinates for 'X' (row and column): ").split())
        board[x][y] = 'X'
        print_board(board)

        # Player O's move (Minimax algorithm)
        print("Player O's move:")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'O'
        print_board(board)

    # Final state of the board
    print("Final Board:")
    print_board(board)

if __name__ == "__main__":
    main()
