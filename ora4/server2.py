import socket
import select
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 10010))
sock.listen(1)

secret_number = random.randrange(1, 100)
inputs = [sock]
while True:
    readable, writeable, ex = select.select(inputs,inputs,inputs)

    for s in readable:
        if s is sock:
            client, addr = s.accept()
            print "Jott egy kliens"
            print secret_number
            inputs.append(client)
        else:
            gussed_num = int(s.recv(1024))
            if gussed_num < secret_number:
                s.send('Gondolj nagyobbra!')
            elif gussed_num > secret_number:
                s.send('Gondolj kisebbre!')
            else:
                s.send('Grat')
                s.close()
                inputs.remove(s)
