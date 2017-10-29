import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',10010)
connection.connect(server_address)
connection.sendall('Hello szerver')
data = connection.recv(16)

print data
connection.close()
