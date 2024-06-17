import math

# Constants for the game
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Initialize the board
def init_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if the game has a winner
def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

# Check for a tie
def check_tie(board):
    return all(EMPTY not in row for row in board)

# Get all possible moves
def get_empty_cells(board):
    return [(x, y) for x in range(3) for y in range(3) if board[x][y] == EMPTY]

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if check_tie(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for (x, y) in get_empty_cells(board):
            board[x][y] = AI
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[x][y] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for (x, y) in get_empty_cells(board):
            board[x][y] = HUMAN
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[x][y] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Determine the best move for the AI
def best_move(board):
    best_val = -math.inf
    move = None
    for (x, y) in get_empty_cells(board):
        board[x][y] = AI
        move_val = minimax(board, 0, -math.inf, math.inf, False)
        board[x][y] = EMPTY
        if move_val > best_val:
            best_val = move_val
            move = (x, y)
    return move

# Main function to play the game
def play():
    board = init_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Human's turn
        while True:
            try:
                x, y = map(int, input("Enter your move (row and column): ").split())
                if board[x][y] != EMPTY:
                    print("Invalid move! Try again.")
                else:
                    board[x][y] = HUMAN
                    break
            except ValueError:
                print("Invalid input! Enter row and column as integers separated by space.")

        print_board(board)
        
        if check_winner(board, HUMAN):
            print("Congratulations! You win!")
            break
        if check_tie(board):
            print("It's a tie!")
            break
        
        # AI's turn
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = AI
            print("AI's move:")
            print_board(board)
            
            if check_winner(board, AI):
                print("AI wins!")
                break
            if check_tie(board):
                print("It's a tie!")
                break

# Run the game
if __name__ == "__main__":
    play()
