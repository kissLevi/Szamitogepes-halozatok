import socket
import struct
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

multicast_group = '224.3.29.71'
server_address = ('', 10000)
sock.bind(server_address)

group = socket.inet_aton(multicast_group) 		# '\xe0\x03\x1dG'
mreq = struct.pack('4sL', group, socket.INADDR_ANY)	# '\xe0\x03\x1dG\x00\x00\x00\x00'
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print ('Waiting to receive message')
data, server_address = sock.recvfrom(4096)
print ("Incoming message from", server_address)
print ("Message:", data)

sock.sendto('Acknowledgement'.encode(), server_address)

sock.close()
