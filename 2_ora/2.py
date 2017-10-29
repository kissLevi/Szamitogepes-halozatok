import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',10010)
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_adress = sock.accept()
    data = connection.recv(16)
    print data
    connection.sendall('Hello kliens')
    connection.close()
sock.close()

