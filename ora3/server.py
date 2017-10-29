import socket
import struct


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

connection, client_address = sock.accept()
data = connection.recv(16)
(sz1,op,sz2) = struct.unpack('i1si',data)

print(sz1,op,sz2)

print data




connection.sendall('Hello kliens')
connection.close()
sock.close()
