import socket
import select
import sys
import re
import time

starttime=time.time()


server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('',12345))
server_sock.listen(1)

sockets = [server_sock, sys.stdin]
clients = []


numberOfClients = 0

chipSequences = [(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0)]


clientsNameAndChips = {}

msgToSend = []


def processMsgs(msg):
    outPut = []
    msgs = msg[1:len(msg)-1]
    msgs = re.split('],?.?',msgs)
    for msg in msgs:
        if msg is not "":
            intBits = []
            bits = (msg[1:].split(", "))
            for bit in bits:
                intBits.append(int(bit))
            outPut.append(intBits)
    return outPut

starttime=time.time()

while True :
    
    if((time.time()-starttime)%60 > 30) and numberOfClients is not 0:
        print(len(msgToSend) is not 0)
        if len(msgToSend) is not 0:
            print("send")
            for c in clients:
                c.send(str(msgToSend))
        starttime = time.time()
        msgToSend = []

    else:
        readable, writeable, ex = select.select(sockets,[],[])
        for r in readable:
            print(type(r))
            if r == sys.stdin:
                server_sock.close()
                for c in clients:
                    c.send("CLOSECONNECTION")
                exit()
            
            elif r == server_sock :
                if numberOfClients == 4:
                    client, addr = r.accept()
                    client.send("CLOSECONNECTION")
                elif numberOfClients<4:
                    client, addr = r.accept()
                    sockets.append(client)
                    clients.append(client)
                    data = client.recv(1024)
                    clientsNameAndChips[data] = chipSequences[numberOfClients]
                    client.send(str(chipSequences[numberOfClients]))
                    numberOfClients+=1
                    print numberOfClients
            
            else:
                print(r == server_sock)
                print(type(r))
                data = r.recv(1024).split(" ")
                if not data :
                    r.close()
                    sockets.remove(r)
                    clients.remove(r)
                elif len(data) == 1:
                    if data[0] is( "exit" or "EXIT"):
                        r.close()
                        sockets.remove(r)
                        clients.remove(r)
                    elif data[0] in clientsNameAndChips:
                        r.send(str(clientsNameAndChips[data[0]]))
                        msg = r.recv(1024)
                        processedmsgs = processMsgs(msg)
                        if len(msgToSend) is 0:
                            msgToSend = processedmsgs
                        else:
                            for i in range(0,len(msgToSend)):
                                for j in range(0,len(msgToSend[i])):
                                    msgToSend[i][j]+=processedmsgs[i][j]
                        # print(msgToSend)
                        # for c in clients:
                        #     c.send(str(msgToSend))
                        
                    else:
                        r.send("BADADRESS")
        


    
        
  

    
    