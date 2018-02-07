#Bit Manipulation: Lonely Integer


#!/bin/python

import sys

def lonely_integer(a):
    if len(a) == 1: return a[0]
    else:
        result = 0
        for i in a:
            result ^= i
        return result


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)
