import socket
import select
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',12345))

sockets = [sock,sys.stdin]

while True:
    readable, w,w = select.select(sockets,[],[])

    for r in readable:
        if r == sys.stdin:
            sock.send(sys.argv[1] + " " + raw_input())
        else:
            data = sock.recv(1024)
            print data