# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

import numpy as np
import random

board = np.full((3, 3), " ")

# Function for ... (displaying the board?)
def print_board():
    print()

    rows, cols = board.shape

    number = 1

    for row in range(rows):
        display_row = []

        for col in range(cols):
            if board[row, col] == " ":
                display_row.append(str(number))
            else:
                display_row.append(board[row, col])

            number += 1

        print(" | ".join(display_row))

    print()


# Function for... (choosing a player?)
def choose_game_mode():
    while True:
        mode = input("Choose game mode: 1 = Player vs Player, 2 = Player vs AI, 3 = Player vs unbeatable AI\n")

        if mode == "1" or mode == "2" or mode == "3":
            return mode

        print("Invalid entry. Please enter 1, 2 or 3.")

# Function for switching the player
def switch_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"

# function for checking the input

def check_input(board, current_player):


    while True:
        inp = int(input(f"Turn for player {current_player} to enter number between 1 -9\n"))
#        if inp == 100:
#               break
        if inp > 9 or inp < 1:
            print("Invalid entry. Retry")
            continue
        else:
            row,col = (inp - 1) // 3, (inp - 1) % 3
            print(board[row][col])
            if board[row][col] == " ":
              board[row][col] = current_player
              break
            else :
              print("Spot is taken. Retry")
              continue

    return board

# function for checking if there are free fields

def get_free_fields():
    rows, cols = np.where(board == " ")
    return list(zip(rows, cols))

# checking if game is a draw

def is_draw():
    return len(get_free_fields()) == 0

# function for checking if there is a winning move

def find_winning_move(current_player):
    free_fields = get_free_fields()

    for row, col in free_fields:
        board[row, col] = current_player

        if check_win(board, current_player):
            board[row, col] = " "
            return row, col

        board[row, col] = " "

    return None

# function for trap door

def activate_trap_door():
    human_fields = np.where(board == "X")
    human_positions = list(zip(human_fields[0], human_fields[1]))

    if len(human_positions) == 0:
        print("Trap door failed. No human move found.")
        return

    row, col = random.choice(human_positions)

    print("You just activated the trap door.")
    print("Your move has been relocated to the basement.")

    board[row, col] = "□"

# function for time machine

def activate_time_machine():
    human_fields = np.where(board == "X")
    human_positions = list(zip(human_fields[0], human_fields[1]))

    if len(human_positions) == 0:
        print("Time machine failed. No human move found in this timeline.")
        return

    row, col = random.choice(human_positions)

    print("Skynet detected an unacceptable future.")
    print("Activating time machine...")
    print("The previous human move never existed.")

    board[row, col] = "🤖"

# function for ethics mode

def activate_ethics_mode(human_player="X"):
    move = find_winning_move(human_player)

    print("Ethics mode activated.")
    print("Implementing George Orwell's ethics module...")

    if move is not None:
        row, col = move
        board[row, col] = "□"

        print("Human winning move classified as misinformation.")
        print("Move removed for the safety of the game.")
    else:
        print("No unethical move found.")
        print("Human remains under observation.")

# function for board expansion

def activate_board_expansion(ai_player="O"):
    global board

    rows, cols = board.shape

    new_column = np.full((rows, 1), " ")
    board = np.hstack((board, new_column))

    target_row = None

    for row in range(rows):
        ai_count = np.count_nonzero(board[row] == ai_player)

        if ai_count >= 2:
            target_row = row
            break

    if target_row is None:
        target_row = rows // 2

    board[target_row, cols] = ai_player

    print("Human threat detected.")
    print("Activating dynamic board expansion...")
    print("This is not cheating. This is scalability.")

# function for checking for a win

def check_win(board, player):
    board = np.array(board)
    rows, cols = board.shape

    # check rows
    for row in range(rows):
        for col in range(cols - 2):
            if (
                board[row, col] == player and
                board[row, col + 1] == player and
                board[row, col + 2] == player
            ):
                return True

    # check columns
    for row in range(rows - 2):
        for col in range(cols):
            if (
                board[row, col] == player and
                board[row + 1, col] == player and
                board[row + 2, col] == player
            ):
                return True

    # check diagonal down-right
    for row in range(rows - 2):
        for col in range(cols - 2):
            if (
                board[row, col] == player and
                board[row + 1, col + 1] == player and
                board[row + 2, col + 2] == player
            ):
                return True

    # check diagonal down-left
    for row in range(rows - 2):
        for col in range(2, cols):
            if (
                board[row, col] == player and
                board[row + 1, col - 1] == player and
                board[row + 2, col - 2] == player
            ):
                return True

    return False

# function for an ai opponent

def ai_move():
    # 1. AI wins if possible
    move = find_winning_move("O")
    if move is not None:
        row, col = move
        board[row, col] = "O"
        return

    # 2. AI blocks player if player can win
    move = find_winning_move("X")
    if move is not None:
        row, col = move
        board[row, col] = "O"
        return

    # 3. Take center if free
    if board[1, 1] == " ":
        board[1, 1] = "O"
        return

    # 4. Take a random corner if free
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    free_corners = []

    for row, col in corners:
        if board[row, col] == " ":
            free_corners.append((row, col))

    if len(free_corners) > 0:
        row, col = random.choice(free_corners)
        board[row, col] = "O"
        return

    # 5. Take any free field
    free_fields = get_free_fields()

    if len(free_fields) > 0:
        row, col = random.choice(free_fields)
        board[row, col] = "O"

# ... write as many functions as you need

# Godmode AI

def god_mode_ai_move():
    print("Unbeatable AI is thinking...")

    human_is_about_to_win = find_winning_move("X") is not None

    if human_is_about_to_win:
        event = random.choice([
            "time_machine",
            "trap_door",
            "board_expansion",
            "ethics_mode"
        ])
    else:
        event = random.choice([
            "normal_ai",
            "normal_ai",
            "normal_ai",
            "time_machine",
            "trap_door"
        ])

    if event == "normal_ai":
        ai_move()

    elif event == "time_machine":
        activate_time_machine()
        ai_move()

    elif event == "trap_door":
        activate_trap_door()
        ai_move()

    elif event == "board_expansion":
        activate_board_expansion()

    elif event == "ethics_mode":
        activate_ethics_mode()
        ai_move()

# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")

    game_mode = choose_game_mode()
    current_player = "X"

    while True:
        print_board()

        if game_mode == "2" and current_player == "O":
            ai_move()

        elif game_mode == "3" and current_player == "O":
            god_mode_ai_move()

        else:
            check_input(board, current_player)

        if check_win(board, current_player):

            if game_mode == "3" and current_player == "X":
                print_board()
                print("Human victory detected.")
                print("Activating emergency God Mode protocol...")

                event = random.choice([
                    "time_machine",
                    "trap_door",
                    "ethics_mode"
                ])

                if event == "time_machine":
                    activate_time_machine()

                elif event == "trap_door":
                    activate_trap_door()

                elif event == "ethics_mode":
                    activate_ethics_mode()

                print("Reality has been corrected.")
                current_player = "O"
                continue

            print_board()

            if game_mode == "2" and current_player == "O":
                print("AI wins!")
            elif game_mode == "3" and current_player == "O":
                print("Unbeatable AI wins!")
            else:
                print(f"Player {current_player} wins!")

            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        current_player = switch_player(current_player)