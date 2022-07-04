from time import sleep

# Too complicated and looks ugly. The players need to see the board.
# board = {
#     "S1": 0, "S2": 0, "S3": 0,
#     "S4": 0, "S5": 0, "S6": 0,
#     "S7": 0, "S8": 0, "S9": 0
# }

board_lst = [
    ["_"], ["_"], ["_"],
    ["_"], ["_"], ["_"],
    ["_"], ["_"], ["_"]
]

# most of my problems in writing functions could have been avoided if I used
# global function inside to call my variable, without needing to make it
# a parameter and writing it in every time.

# have to make it look acceptable! code might be bad. (also overcomplicated)
# Could've simply used the Print function three times.
def print_board(board):
    result = ""
    for square in board:
        if square is board[2] or square is board[5] or square is board[8]:
            result += f"{square} \n"
        else:
            result += f"{square}"
    print(result)


def reset_board(board):
    i = 0
    for square in board:
        if square is not ["_"]:
            board[i] = ["_"]
            i += 1


def help_me():
    print("Your choices are:")
    print("[1] [2] [3] \n[4] [5] [6] \n[7] [8] [9]")


# simple input loop for either symbols.
def place_symbol(symbol):
    spot = input("Enter any number from 1 to 9.\n>")
    try:
        if spot in str([1, 2, 3, 4, 5, 6, 7, 8, 9]) \
                and board_lst[int(spot) - 1] == ["_"]:
            board_lst[int(spot) - 1][0] = symbol
            return True
        else:
            print("invalid input! please try again!")
            help_me()
            return place_symbol(symbol)
    except ValueError:
        print("Silence will not save you here! YOU MUST CHOOSE!")
        return place_symbol(symbol)


# Check if symbol is in a winning pattern, did it like this to make writing
# The next function easier.
def win_pattern(symbol, num1, num2, num3):
    return symbol in board_lst[num1] \
           and symbol in board_lst[num2] \
           and symbol in board_lst[num3]


# Check after a player's move is over.
def is_it_over(char):
    # Slash Line Wins.
    if win_pattern(char, 0, 4, 8) \
            or win_pattern(char, 2, 4, 6):
        return True
    # Horizontal Line Wins.
    elif win_pattern(char, 0, 1, 2) \
            or win_pattern(char, 3, 4, 5) \
            or win_pattern(char, 6, 7, 8):
        return True
    # Vertical Line Wins.
    elif win_pattern(char, 0, 3, 6) \
            or win_pattern(char, 1, 4, 7) \
            or win_pattern(char, 2, 5, 8):
        return True


# This used to be how I wrote it before, however: Attribute Error: __enter__
# I am keeping it in because I still don't understand the error, and hope
# That someone may be able to explain it to me. I'll look it up too.
# def is_it_over(symbol):
#     with board_lst as b:
#         with symbol as s:
#             # Slash Line Wins
#             if (s in b[0] and s in b[4] and s in b[8]) \
#                     or (s in b[2] and s in b[4] and s in b[6]):
#                 return True
#             # Horizontal Line Wins
#             elif (s in b[0] and s in b[1] and s in b[2]) \
#                     or (s in b[3] and s in b[4] and s in b[5]) \
#                     or (s in b[6] and s in b[7] and s in b[8]):
#                 return True
#             # Vertical Line Wins
#             elif (s in b[0] and s in b[3] and s in b[6]) \
#                     or (b[1] and s in b[4] and s in b[7]) \
#                     or (b[2] and s in b[5] and s in b[8]):
#                 return True
#             elif [] not in b:
#                 print("It's a Draw.")
#                 end()
#             else:
#                 return False


def game_loop(board):
    p1 = True
    p2 = False
    while ["_"] in board:
        print_board(board)
        if p1:
            # This needs to be made a function.. I'm
            # unsure if it'd make a difference though.
            played = place_symbol("O")
            if played:
                if is_it_over("O"):
                    print_board(board)
                    print("Player 1 Wins.")
                    return end()
                print("It is now Player 2's turn.")
                p2 = True
                p1 = False
        elif p2:
            played = place_symbol("X")
            if played:
                if is_it_over("X"):
                    print_board(board)
                    print("Player 2 Wins.")
                    return end()
                else:
                    print("It is now Player 1's turn.")
                    p1 = True
                    p2 = False

        if ["_"] not in board:
            print_board(board_lst)
            print("It's a Draw.")
            return end()


def end():
    play_again = input("Play again? y/n\n>")
    while play_again.lower() not in ["yes", "no", "y", "n"]:
        play_again = input("Not a valid answer, play again?\n>")
    if play_again.lower() in ["yes", "y"]:
        reset_board(board_lst)
        return game_loop(board_lst)
    else:
        print("Ok, bye!")
        exit()


def main_menu():
    print("Hi, this is literally just tic tac toe.")
    choice = input("Type what you want: \n1. Play\n2. Help\n3. Quit\n> ")
    while choice.lower() not in ["play", "help", "quit"]:
        print("Nope, not a valid command, try again.")
        return main_menu()
    if choice.lower() == "play":
        print("Ok! Great! Bring someone to play with.")
        return game_loop(board_lst)
    elif choice.lower() == "help":
        help_me()
        sleep(3)
        return main_menu()
    elif choice.lower() == "quit":
        print("Ok, bye!")
        exit()


main_menu()
