#!/usr/bin/env python3.6

message = input("What would you like me to repeat? ")
timer = input("How many time do you want it repeated? ")

def inputEcho(echo, counter):
    count = 0
    while counter > count:
        print(echo)
        count += 1

inputEcho(message, int(timer))
