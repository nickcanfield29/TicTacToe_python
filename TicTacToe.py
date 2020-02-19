def is_there_a_winner(board):
    xcount = 0
    ocount = 0
    if (board[0] == board[1] == board[2]) or (board[3] == board[4] == board[5]) or (board[6] == board[7] == board[8]) or (board[0] == board[3] == board[6]) or (board[1] == board[4] == board[7]) or (board[2] == board[5] == board[8]) or (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]):
        for position in board:
            if position.lower() == 'x':
                xcount += 1
            elif position.lower() == 'o':
                ocount += 1
        if xcount > ocount:
            return 'x'
        else:
            return 'o'


def print_board(board):
    print('-------------------')
    print('| ', board[0], ' | ', board[1], ' | ', board[2], ' |')
    print('-------------------')
    print('| ', board[3], ' | ', board[4], ' | ', board[5], ' |')
    print('-------------------')
    print('| ', board[6], ' | ', board[7], ' | ', board[8], ' |')
    print('-------------------')

def play_turn(board):
    xcount = 0
    ocount = 0
    quit = False
    while quit == False:
        for position in board:
            if position.lower() == 'x':
                xcount += 1
            elif position.lower() == 'o':
                ocount += 1

        if xcount > ocount:
            player = 'O'
            print('\n')
            print_board(board)
            print("\nO, it's your turn")
            choice = int(input("What position do you want\n"))
        else:
            player = 'X'
            print('\n')
            print_board(board)
            print("\nX, it's your turn")
            choice = int(input("What position do you want\n"))

        if choice not in range(1, 9):
            print("Not a valid number, bad boy!")
        elif board[choice - 1] in ['X', 'O']:
            print("\nPlace already taken.")
            print("Choose another square")
        else:
            quit = True

    return [choice, player]

def print_game_count(x_wins, o_wins):
    print('\n')
    print("X Wins: ", x_wins)
    print("O Wins: ", o_wins)
    print('\n')

def play_game():
    x_wins = 0
    o_wins = 0

    quit1 = False
    while quit1 == False:
            initial_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            board = initial_board
            if x_wins == 0 and o_wins == 0:
                print("Do you want to play tic tac toe?")
            else:
                print("Want to play again?")
            start_game = input("Press y for yes. n for no\n")
            if start_game.lower() in ['y', 'yes']:
                quit2 = False
                while quit2 == False:
                    if is_there_a_winner(board) == 'x':
                        print('\n')
                        print(is_there_a_winner(board).upper(), " wins!")
                        x_wins += 1
                        print_game_count(x_wins, o_wins)
                        quit2 = True
                    elif is_there_a_winner(board) == 'o':
                        print('\n')
                        print(is_there_a_winner(board).upper(), " wins!")
                        o_wins += 1
                        print_game_count(x_wins, o_wins)
                        quit2 = True
                    else:
                        choice = play_turn(board)
                        board[choice[0] - 1] = choice[1]

            else:
                print('\n')
                print("Thanks for playing!")
                print_game_count(x_wins, o_wins)
                quit1 = True

play_game()

