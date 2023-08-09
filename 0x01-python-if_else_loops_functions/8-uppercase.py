#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            chk = ord(c) - 32
        else:
            chk = ord(c)
        print("{:c}".format(chk), end='')
    print("")
