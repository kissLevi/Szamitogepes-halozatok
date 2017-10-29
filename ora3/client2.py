import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('157.181.163.135', 12345)
sock.sendto(":(",server_address)
data, addr = sock.recvfrom(1024)
print(data)


