import connectfour
from collections import namedtuple

def print_board(game_state) -> None:
    '''prints the entire connect four board based on the current game state'''
    
    board: str = ''
    rows = len(game_state.board[0])
    columns = len(game_state.board)
    for i in range(1,columns+1):
        if i < 9:
            board += str(i)
            board += '   '
        else:
            board += str(i)
            board += '  '
    board += '\n'
    for i in range(rows):
        for j in range(columns):
            if game_state.board[j][i] == 0:
                board += '.   '
            else:
                if game_state.board[j][i] == 1:
                    board += 'R   '
                else:
                    board += 'Y   '
    
        board += '\n'
    print(board)

def red_turn(game_state, move: str) -> 'Gamestate' or None:
    '''first checks for win condition. if neither player has won, updates the board with red's move'''
    
    win = check_win_condition(game_state)
    if win == 'win':
        return None
    #col_red = input("(Type a 'DROP' followed by a column number if you want to drop a piece at that specific column,or type 'POP' followed by a column number to pop out your piece at that specific column): ")
    if move[0:move.index(' ')] == 'POP':
        print("Pop")
        return connectfour.pop(game_state, int(move[4:])-1))
    elif move[0:move.index(' ')] == 'DROP':
         print("Drop")
        return connectfour.drop(game_state, int(move[5:])-1))
    else:
        pass
##  print_board(current_game_state)

def yellow_turn(game_state)->'Gamestate' or None:
    '''first checks for win condition. if neither player has won, updates the board with yellow's move'''
    
    win = check_win_condition(game_state)
    if win == 'win':
        return None 
    col_yellow = input("Yellow's Turn(Type a column number if you want to drop a piece at that specific column, or type 'p' followed by a column number to pop out your piece): ")
    if col_yellow[0] == 'p':
        return connectfour.pop(game_state, int(col_yellow[1:])-1)
    else:    
        return connectfour.drop(game_state, int(col_yellow)-1)
##    print_board(current_game_state)
 
def check_win_condition(game_state) -> str or None:
    '''checks which player has won, if any. If not, nothing happens.'''
    
    winner = connectfour.winner(game_state)
    if winner == 1:
        print('Congratulations RED, you win!')
        return 'win'
    elif winner == 2:
        print('Congratulations YELLOW, you win!')
        return 'win'
    else:
        pass
