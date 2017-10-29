#!/usr/env/python

ev = 200

def szokoev(ev):
    if(ev%4 == 0 and ev%400 == 0):
        print "szokoev"
    else:
        print "nem szokoev"
szokoev(ev)
