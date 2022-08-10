import random


# This script will run an interactive tic-tac-toe game


# Display a game board template
def game_board_template():
    print('\nThese are the corresponding cells & numbers')
    print('_1_|_2_|_3_')
    print('_4_|_5_|_6_')
    print(' 7 | 8 | 9 ')
    print('\n')


def game_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    return board


def clear_screen():
    print('\n'*100)


def player_marker():
    marker = ''
    marker = input('\nPlayer 1, do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board,marker,position):
    board[position] = marker
    return board


def win_checker(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    player_list = [1,2]
    random.shuffle(player_list)
    if player_list[0] == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board,position):
    return board[position] == ' '


def full_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    choice = 0
    acceptable_range = range(1, 10)
    choice = input('Please choose your next space (1-9): ')
    if choice.isdigit() == False:
        print('That was not a digit')
        player_choice(board)
    else:
        if int(choice) in acceptable_range:
            return int(choice)
        else:
            print('That was not between 1 and 9')

    if space_check(board,choice) == True:
        return choice
    else:
        print('That space is not available. Choose an open space')
        player_choice(board)


def play_again():
    return input('Do you want to play again? Y or N: ').upper().startswith('Y')


print('Welcome to Tic-Tac-Toe!')

while True:
    startBoard = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker, player2_marker = player_marker()
    turn = choose_first()
    print(turn, 'goes first. Good luck!')

    game_start = input('Are you ready to begin? Y or N: ').upper()
    if game_start == 'Y':
        play_game = True
    else:
        play_game = False
        print('Goodbye')
        exit(99)

    while play_game == True:
        if turn == 'Player 1':
            game_board_template()
            game_board(startBoard)
            print('Player 1 turn')
            position = player_choice(startBoard)
            while space_check(startBoard,position) == False:
                print('That space is taken. Try again.')
                position = player_choice(startBoard)
            else:
                place_marker(startBoard,player1_marker,position)
            if win_checker(startBoard,player1_marker):
                clear_screen()
                print('Player 1 wins!')
                game_board(startBoard)
                play_game = False
            else:
                if full_check(startBoard):
                    clear_screen()
                    game_board(startBoard)
                    print("It's a draw")
                    break
                else:
                    clear_screen()
                    turn = 'Player 2'


        else:
            game_board_template()
            game_board(startBoard)
            print('Player 2 turn')
            position = player_choice(startBoard)
            while space_check(startBoard, position) == False:
                print('That space is taken. Try again.')
                position = player_choice(startBoard)
            else:
                place_marker(startBoard, player2_marker, position)
            if win_checker(startBoard,player2_marker):
                clear_screen()
                print('Player 2 wins!')
                game_board(startBoard)
                play_game = False
            else:
                if full_check(startBoard):
                    clear_screen()
                    game_board(startBoard)
                    print("It's a draw")
                    break
                else:
                    clear_screen()
                    turn = 'Player 1'
    if not play_again():
        print('Goodbye!')
        break
