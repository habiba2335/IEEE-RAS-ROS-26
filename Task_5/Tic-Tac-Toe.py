def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]             
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    p1_symbol = ""
    while p1_symbol not in ['X', 'O']:
        p1_symbol = input("Player 1, choose your symbol (X or O): ").upper()
    
    p2_symbol = 'O' if p1_symbol == 'X' else 'X'
    print(f"Player 1 is {p1_symbol}, Player 2 is {p2_symbol}")
    
    current_player = p1_symbol
    turns = 0
    
    while turns < 9:
        print_board(board)
        
        if current_player == 'X':
            color = "\033[91m" # Red
        else:
            color = "\033[94m" # Blue
            
        move_str = input(f"{color}Player {current_player}\033[0m, choose a position (1-9): ")
            
        if not move_str.isdigit():
            print("Invalid input! Enter a number.")
            continue
            
        move = int(move_str) - 1
        
        if move < 0 or move > 8:
            print("Position out of range! Choose from 1 to 9.")
            continue
            
        if board[move] in ['X', 'O']:
            print("Position already taken! Choose a different one.")
            continue
            
        board[move] = current_player
        turns += 1
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"*** Player {current_player} wins! ***")
            return
            
        current_player = p2_symbol if current_player == p1_symbol else p1_symbol
        
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()