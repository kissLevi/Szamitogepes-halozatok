#!/usr/env/python

ev = 100

def szokoev(ev):
    if(ev%4 == 0):
        if((num %100) ==0) and ((num%400) != 0):
            print "new szokoev"
    else:
        print "nem szokoev"



def alarm_clock(day,vacation):
    if(vacation ==True):
        if day<5:
            print "10:00"
        else:
            print "OFF"
    else:
        if day<5:
            print "7:00"
        else:
            print "10:00"

alarm_clock(0,True)

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
print fibonacci(0)

print fibonacci(1)
print fibonacci(4)
