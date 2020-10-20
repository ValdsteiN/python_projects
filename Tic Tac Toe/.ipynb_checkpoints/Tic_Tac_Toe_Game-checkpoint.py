import random

def display_board(board=None):
    if board is None:
        board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]  }"
          f"\n------------------"
          f"\n  {board[4]}  |  {board[5]}  |  {board[6]  }"
          f"\n------------------"
          f"\n  {board[7]}  |  {board[8]}  |  {board[9]  }")
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

#game_board = ["#"," "," "," "," "," "," "," "," "," "]

def player_input():
    assignment = True
    while assignment:
        markers = ["O", "X"]
        query1 = int(input("\nPlayer 1, please select your token. Type 0 (zero) for playing with 'O' marker or type 1 for playing with 'X' marker --> "))
        player1_token = markers[query1]
        print(f"\nPlayer 1, you have assigned a {markers[query1]} token for yourself.")
        markers.pop(query1)
        print(f"Player 2, your token is {markers[0]} for the game.")
        player2_token = markers[0]
        assignment = False
    return (player1_token, player2_token)

def place_marker(board, marker, position):
    print(f"Please, put your token on the desired position from 1 to 9")
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
"""
# def win_check(board):
#     ok = False
#     lala = []
#     for i in range(len(board)):
#         if i is not None:
#             lala.append("okay")
#         else:
#             lala.append("nok")
#     if "nok" not in lala:
#         ok = True
#     if ok:
#         if (board[1] == board[2] == board[3]) or (board[4] == board[5] == board[6]) or (board[7] == board[8] == board[9]) or (board[2] == board[5] == board[8]) or\
#                 (board[3] == board[6] == board[9]) or (board[1] == board[4] == board[7]) or (board[1] == board[5] == board[9]) \
#                 or (board[3] == board[5] == board[7]):
#             return True
#         else:
#             return False

# def win_check(board):
#     if (board[1] == board[2] == board[3]) or (board[4] == board[5] == board[6]) or (board[7] == board[8] == board[9]) or (board[2] == board[5] == board[8]) or\
#             (board[3] == board[6] == board[9]) or (board[1] == board[4] == board[7]) or (board[1] == board[5] == board[9]) \
#             or (board[3] == board[5] == board[7]):
#         return True
#     else:
#         return False
"""
def choose_first():
    players = ["Player 1", "Player 2"]
    chosen = players[random.randint(0,1)]
    print(f"\nIt was randomly decided that {chosen} goes first!")
    return chosen

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Type in your next position to place the marker. Choose the  number from 1 to 9 --> "))

    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

"""----------------------------------------------------------------------------------------------------------
"""

print("Welcome to Tic-Tac-Toe!")

while True:
    print('\n' * 10)
    game_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    player1_badge, player2_badge = player_input()
    current_turn = choose_first()
    print(f'\n{current_turn} goes first!')

    cont = input("\nAre you ready to start the game with the set parameters? Type 'Yes' or 'No' --> ")
    if cont.lower() == "yes":
        game_on = True
    else:
        game_on = False

    while game_on:
        if not full_board_check(game_board):
            if current_turn == "Player 1":
                display_board(game_board)
                place_marker(game_board,player1_badge,player_choice(game_board))

                if win_check(game_board, player1_badge):
                    display_board(game_board)
                    print("\nCongratulations, Player 1! You have won the game!")
                    game_on = False
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print("\nOops, that's a draw!")
                        break
                    else:
                        current_turn = "Player 2"
            else:
                display_board(game_board)
                place_marker(game_board, player2_badge, player_choice(game_board))

                if win_check(game_board, player2_badge):
                    display_board(game_board)
                    print("\nCongratulations, Player 2! You have won the game!")
                    game_on = False
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print("\nOops, that's a draw!")
                        break
                    else:
                        current_turn = "Player 1"
    if not replay():
        break