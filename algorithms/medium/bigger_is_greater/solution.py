#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#
 
def biggerIsGreater(w):
    chars = list(w)
    
    l = []
    
    min_j = None
    
    for i in range(len(chars) - 1, 0, -1):
        char = chars[i]
        for j in range(i - 1, -1, -1):
            char2 = chars[j]
            if char > char2:
                if min_j == None or j <= min_j:
                    min_j = j 
                    l.append((j, i, char))
                    
    
    l = list(filter(lambda x : x[0] == min_j, l))   
                
    if len(l) <= 0:
        return "no answer"
    
    if len(l) > 1:
        print(l)
        l.sort(key=lambda x : x[2])
    
    swap = l[0]
    
    chars[swap[1]] = chars[swap[0]]
    chars[swap[0]] = swap[2]
    
    return "".join(chars)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
