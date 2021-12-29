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
        print('game won')
    if move[0:move.index(' ')] == 'POP':
        return connectfour.pop(game_state, (int(move[4:]))-1)
    
    elif move[0:move.index(' ')] == 'DROP':
        return connectfour.drop(game_state, (int(move[5:]))-1)
    
    else:
        pass

def yellow_turn(game_state, move: str)->'Gamestate' or None:
    '''first checks for win condition. if neither player has won, updates the board with yellow's move'''
##    print(f'yellow move: {move}')
    win = check_win_condition(game_state)
    if win == 'win':
##        print('game won')
        return None 
    if move[0:move.index(' ')] == 'POP':
        return connectfour.pop(game_state, (int(move[4:]))-1)
    
    elif move[0:move.index(' ')] == 'DROP':
        return connectfour.drop(game_state, (int(move[5:]))-1)
    
    else:
        pass
 
def check_win_condition(game_state) -> str or None:
    '''checks which player has won, if any. If not, nothing happens.'''
    
    winner = connectfour.winner(game_state)
    if winner == 1:
        print('Congratulations RED wins!')
        return 'win'
    elif winner == 2:
        print('Congratulations YELLOW wins!')
        return 'win'
    else:
        pass
