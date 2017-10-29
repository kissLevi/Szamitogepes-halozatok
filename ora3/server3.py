import socket
import struct
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

multicast_group_address = ('224.3.29.71', 10000)

sock.settimeout(3)

ttl = struct.pack('b', 1) # '\x01'
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
  sock.sendto('Hello clients'.encode(), multicast_group_address)
  
  while True:
    try:
      data, client_address = sock.recvfrom(4096)
    except socket.timeout:
       print ('timed out, no more responses')
       break
    else: # executed code if there is no exception in the try clause
       print ("Incoming message from", client_address)
       print ("Message:", data)
finally:
  print ('closing socket')
  sock.close()
