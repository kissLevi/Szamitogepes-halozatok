import socket
import struct


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
connection.connect(server_address)

packed_data = struct.pack('I1sI',12,'+',24)

connection.sendall(packed_data)
data = connection.recv(16)

print data
connection.close()
