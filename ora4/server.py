import socket
import struct
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10010)
sock.bind(server_address)
sock.listen(1)

number = random.randrange(1, 100)
connection, client_address = sock.accept()
data = int(connection.recv(1024))
#(sz1,op,sz2) = struct.unpack('i1si',data)


#print(sz1,op,sz2)
#while data != number:
#print "nem jo"
if number < data:
    connection.send('Gondolj nagyobbra!')
elif data > number:
    connection.send('Gondolj kisebbre!')
else:
    connection.send('Grat')
    sock.close()
    connection.close()

# print number
# if data == number:
#     connection.sendall('')
#     connection.close()
#     sock.close()
# else :
#     print "nem jo"
