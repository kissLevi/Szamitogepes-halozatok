import socket
import select
import sys

server_sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('',12345))
server_sock.listen(1)

sockets =[server_sock, sys.stdin]
clients=[]

while True:
    readable, writeable, ex = select.select(sockets,[],[])
    for r in readable:
        if r == sys.stdin:
            server_sock.close()
            exit()
        elif r == server_sock:
            client, addr = r.accept()
            sockets.append(client)
            clients.append(client)
        else:
            data = r.recv(1024)
            if not data :
                r.close()
                sockets.remove(r)
                clients.remove(r)
            else:
                print(data)
                for c in clients:
                    if c != r:
                        c.send(data)