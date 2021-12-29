import socket

sock = socket.socket()
sock.connect(('circinus-32.ics.uci.edu',4444))
inp = sock.makefile('w')
outp = sock.makefile('r')




message = input("Move: ")
inp.write(message + '\r\n')
inp.flush()

print(outp.readline())

message = input("Move: ")
inp.write(message + '\r\n')
inp.flush()

print(outp.readline())

while True:
    message = input("Move: ")
    inp.write(message + '\r\n')
    inp.flush()
    
    a = []
    a.append(outp.readline())
    a.append(outp.readline())
    a.append(outp.readline())
    print(a)
    
