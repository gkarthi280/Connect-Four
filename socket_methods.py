import socket

def connect(host: str, port: int) -> 'connection':
    '''
    Connects to the server, given host and port
    '''
    sock = socket.socket()
    sock.connect((host, port))

    sock_input = sock.makefile('r')
    sock_output = sock.makefile('w')

    return sock, sock_input, sock_output



def close(connection: 'connection') -> None:
    '''
    Closes a connection
    '''

    sock, sock_input, sock_output = connection

  
    sock_input.close()
    sock_output.close()
    sock.close()



def send_move(connection: 'connection', message: str) -> None:
    '''
    Sends a message to the server
    '''
    print(f'sent move: {message}')
    sock, sock_input, sock_output = connection

      
    sock_output.write(message + '\r\n')
    
    sock_output.flush()


   
def receive_response(connection: 'connection') -> str:
    '''
    Receives a response from the server (only one line)
    '''
    sock, sock_input, sock_output = connection
    response = sock_input.readline()
    update_response = response[:-1]
##    print(f'received response: {update_response}')
    return update_response

def receive_move(connection: 'connection') -> list:
    '''
    Receives a move from the server consisting of three lines in the form of a list of strings
    '''
    sock, sock_input, sock_output = connection
    response = sock_input.readlines()
##    print(f'received move: {response}')
    sock_input.flush()
    return response


