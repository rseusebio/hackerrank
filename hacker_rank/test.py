#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accnonDivisibleSubsetepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def isSubsetOk( sub, k ):

    size = len( sub )

    for i in range( size ):
       
        v = sub[ i ]

        for j in range( size ):

            if j == i:
                continue
            
            s = v + sub[ j ]
            if  s % k == 0: 
                return False 

    return True   

def nonDivisibleSubset( k, S ):

    size = len( S )

    for i in range( size, 1, -1 ):

        for c in combinations( S, i ):
            
            if isSubsetOk( c, k ):
                return i

    for i in S:
        if i % k == 0:
            return 1 
            
    return 0

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
