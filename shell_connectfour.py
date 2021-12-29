import connectfour
import ui_connectfour
from collections import namedtuple
current_game_state = ()

    
def connectfour_shell_version() -> None:
    '''shell version of connect four'''
    print('Welcome to Connect Four!')
    columns = int(input('Columns: '))
    rows = int(input('Rows: '))
    current_game_state = connectfour.new_game(columns, rows)
    #print(current_game_state)
    ui_connectfour.print_board(current_game_state)

    
    while True:

        win = ui_connectfour.check_win_condition(current_game_state)
        if win == 'win':
            break
        
        print('RED Move\n_________')
        red_move: str = input("Type 'DROP' followed by a column number if you want to drop a piece at that specific column, or type 'POP' followed by a column number to pop out your piece at that specific column): ")
        
        try:
            current_game_state = ui_connectfour.red_turn(current_game_state, red_move)
            
        except:
            print('Oops! Invalid Move. Please Try Again.')
            continue
        
        else:
            ui_connectfour.print_board(current_game_state)
            pass
            
        win = ui_connectfour.check_win_condition(current_game_state)
        if win == 'win':
            break
        
        print('YELLOW Move\n_________')
        yellow_move: str = input("Type 'DROP' followed by a column number if you want to drop a piece at that specific column, or type 'POP' followed by a column number to pop out your piece at that specific column): ")        
        try:
            current_game_state = ui_connectfour.yellow_turn(current_game_state, yellow_move)
        except:
            print('Oops! Invalid Move. Please Try Again.')
            continue
        else:
            ui_connectfour.print_board(current_game_state)
            pass

if __name__ == '__main__':
    connectfour_shell_version()
