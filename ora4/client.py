import socket
import struct


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10010)
connection.connect(server_address)

won = False
while not won:
    connection.send(str(input('Adj meg egy szamot: ')))
    answer = connection.recv(1024)
    print answer
    won = ("Grat" == answer)
