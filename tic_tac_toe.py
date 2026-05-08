# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)
import random

# Function for ... (displaying the board?)
import numpy as np

def print_board(matrix):
    for row in matrix:
        print("|".join(row))
        print("-------")

# Function for choosing a player
def choose_player():
    print("Please enter your choice: (X or O)")
    player = input()
    return player

def check_win(matrix, player):
    row_win = np.any(np.all(matrix == player, axis=1))
    col_win = np.any(np.all(matrix == player, axis=0))
    diag_win = np.all(np.diag(matrix) == player)
    anti_diag_win = np.all(np.diag(np.fliplr(matrix)) == player)
    return row_win or col_win or diag_win or anti_diag_win

def check_draw(matrix):
    return np.any(np.all(matrix != " "))

def check_input(input, matrix):
    if input[0] > 2 or input[0] < 0 or input[1] > 2 or input[1] < 0:
        return False
    elif matrix[input[0]][input[1]] != " ":
        return False
    else:
        return True

def choose_game_mode():
    while True:
        mode = input("Choose game mode: 1 = Player vs Player, 2 = Player vs Machine\n")

        if mode == "1" or mode == "2":
            return mode

        print("Invalid entry. Please enter 1 or 2.")

def random_move(matrix):
    while True:
        random_move = [random.randint(0, 2), random.randint(0, 2)]
        if check_input(random_move, board):
            return random_move
        else:
            continue

# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    mode = choose_game_mode()
    if mode == "1": # Player vs Player
        player_1 = choose_player()
        if player_1 == "X":
            player_2 = "O"
        else:
            player_2 = "X"
    else:
        player_1 = choose_player()
        player_2 = "🤖"

    board = np.full((3, 3), " ")
    print_board(board)
    total_moves = 0
    while True:
        move = []
        if mode == "1" or (total_moves % 2 == 0 and mode == "2"):
            print(f"Player {(total_moves % 2) + 1}:")
            print("Please enter your move, which row you want to place: (row 1 to 3)")
            move.append(int(input())-1)
            print("Please enter your move, which column you want to place: (column 1 to 3)")
            move.append(int(input())-1)
            if not check_input(move, board):
                print("Invalid move!")
                continue
            if not total_moves % 2:
                board[move[0]][move[1]] = player_1
            else:
                board[move[0]][move[1]] = player_2
            print_board(board)
            if check_win(board, player_1 if not total_moves % 2 else player_2):
                print(f"Player {total_moves % 2 + 1} wins!")
                break
            elif check_draw(board):
                print("We have a draw!")
                break
        elif total_moves % 2 == 1 and mode == "2":
            print("It's the machines turn...")
            move = random_move(board)
            board[move[0]][move[1]] = player_2
            print_board(board)
            if check_win(board, player_1 if not total_moves % 2 else player_2):
                print(f"Player {player_1 if not total_moves % 2 else player_2} wins!")
                break
            elif check_draw(board):
                print("We have a draw!")
                break
        total_moves += 1