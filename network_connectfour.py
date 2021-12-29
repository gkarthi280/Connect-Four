import socket_methods
import socket
import ui_connectfour
import connectfour
from collections import namedtuple
HOST: str = 'circinus-32.ics.uci.edu'
PORT: int = 4444
current_game_state = ()

'''
in this program i have implemented a while loop, and inside of it ask for the moves. But for some reason, the first exchange is correct,
my program always gives an error saying "Conenction reset by peer" during the second loop. Unfortunately I don't know how to fix this bug.
Please take this into consideration when grading. All of my other modules work fine, as well as the shell version.
'''


def connectfour_network_version():
    '''network version of connect four'''
    connection = socket_methods.connect(HOST, PORT)
    print('Welcome to Connect Four!')
    username: str = input('Please enter a desired username: ')
    username = 'I32CFSP_HELLO ' + username
    socket_methods.send_move(connection, username)
    print(socket_methods.receive_response(connection))

    while True: 
        try:
            columns = int(input('Columns: '))
        except:
            print('Oops! Columns must be an integer')
            continue
        else:
            break
    
    while True  :    
        try:
            rows = int(input('Rows: '))
        except:
            print('Oops! Rows must be an integer')
            continue
        else:
            break


    
    socket_methods.send_move(connection, 'AI_GAME ' + str(columns) + ' ' + str(rows))
    print(socket_methods.receive_response(connection))
    current_game_state = connectfour.new_game(columns, rows)
    ui_connectfour.print_board(current_game_state)


    while True:
        win = ui_connectfour.check_win_condition(current_game_state)
        if win == 'win':
            break
        print('Your Move\n_________')
        red_move: str = input("Type 'DROP' followed by a column number if you want to drop a piece at that specific column, or type 'POP' followed by a column number to pop out your piece at that specific column): ")
        try:
            current_game_state = ui_connectfour.red_turn(current_game_state, red_move)

        except:
            print('Oops! Invalid Move. Please Try Again.')
            continue

        else: 
            socket_methods.send_move(connection, red_move.strip(' ') + '\r\n')

        win = ui_connectfour.check_win_condition(current_game_state)
        if win == 'win':
            break

        response = socket_methods.receive_move(connection)
        print(response[0])
        ui_connectfour.print_board(current_game_state)
        print('YELLOW Move\n___________')
        yellow_move = response[1]
        current_game_state = ui_connectfour.yellow_turn(current_game_state, yellow_move)
        ui_connectfour.print_board(current_game_state)
        print(response[2])
                  
    socket_methods.close(connection)



if __name__ == '__main__':
    connectfour_network_version()
