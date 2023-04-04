#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else: 
        s = [0,1]
        i = 1
        while i < length-1:
            next_number = s[i-1] + s[i]
            s.append(next_number)
            i += 1
        print(s)
