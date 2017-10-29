import socket
import select
import sys
import re

def transformChipToInt(data):
    chip = []
    stringChip = data[1:11].split(",")
    for numb in stringChip:
        chip.append(int(numb))
    return chip

def minusChip(chip):
    result = []
    for bit in chip:
        result.append(-1*bit)
    return result

def codeMessage(msg,chip):
    newMsg = []
    for bit in msg:
        if bit == 0:
            newMsg.append(minusChip(chip))
        elif bit == 1:
            newMsg.append(chip)
    return newMsg

def convertMsg(msg):
    result = []
    for bit in msg:
        if int(bit) == 0 or int(bit) == 1:
            result.append(int(bit))
        else:
            return (False,result)

    return(True,result)

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

def decodeMsg(msg,chipCode):
    message = []
    for i in range(0,len(msg)):
        result = 0
        for j in range(0,len(chipCode)):
            result += msg[i][j]*chipCode[j]
        if result < 0:
            message.append(0)
        elif result == 0:
            message.append("N")
        elif result > 0:
            message.append(1)
    return message
        


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',12345))

sockets = [sock,sys.stdin]

chipCode = []

sock.send(sys.argv[1])



while True:
    readable, w,w = select.select(sockets,[],[])

    for r in readable:
        if r == sys.stdin:
            message = raw_input().split(" ")
            #print(message[1].isdigit() is False)
            if ((len(message) is not 2) or (message[1].isdigit() is False)) or len(message[1]) is not 8:
                print("BAD MESSAGE")
            elif len(message) is 2:
                valid, text = convertMsg(message[1])
                if valid:
                    sock.send(message[0])
                    data = sock.recv(1024)
                    adressChip = transformChipToInt(data)
                    sock.send(str(codeMessage(text,adressChip)))
                else:
                    print("BAD MESSAGE")
            # print(sock.recv(1024))
            #  reciverChip = transformChipToInt(sock.recv(1024))
            # print(reciverChip)
            # for char in reciverChip:
            #     print(int(char))
            # sock.send(sys.argv[1] + " " + raw_input())
        else:
            data = sock.recv(1024)
            if data == "CLOSECONNECTION":
                sock.close()
                exit()
            elif len(chipCode) == 0:
                chipCode = transformChipToInt(data)
                #print(chipCode)
                print "Connected"
            else:
                msg = decodeMsg(processMsgs(data),chipCode)
                print(msg)
                # print 
                # asd = []
                # asd = data[1:11].split(",")
                # for s in asd:
                #     print int(s)
                #print int(asd[3])
        

