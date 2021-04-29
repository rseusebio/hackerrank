#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack( n, k, r_q, c_q, obstacles ):

    res = 0

    #print( "up" )
    # all up possibilites
    for i in range( r_q + 1, n + 1 ):

        p = [ i , c_q ]

        #print( p )

        if p in obstacles:

            #print( "{0} is inside".format( p ) )

            obstacles.remove( p )
            
            break

        res += 1
    
    #print( "down" )
    # all down possibilities 
    for i in range( r_q - 1, 0, -1 ):
        
        p = [ i, c_q ]

        #print( p )

        if p in obstacles:

            #print( "{0} is inside".format( p ) )
            
            break

        res += 1

    #print( "right" )
    # all right possibilites 
    for i in range( c_q + 1, n + 1 ):
        
        p = [ r_q, i ]

        #print( p )

        if p in obstacles:

            #print( "{0} is inside".format( p ) )
            
            break

        res += 1
    
    #print( "left" )
    # all left possibilites 
    for i in range( c_q - 1, 0, -1 ):

        p = [ r_q, i ]

        #print( p )

        if p in obstacles:

            #print( "{0} is inside".format( p ) )
            
            break

        res += 1 
    
    #print( "right and up" )
    # rigth and up diagonal 
    c  = c_q + 1
    r  = r_q + 1

    while True:

        if c > n or r > n:
            break

        p = [ r, c ]

        #print( p )

        if p in obstacles:

            #print( "{0} is inside".format( p ) )
            
            break

        res += 1

        c += 1
        r += 1
    
    #print( "left and up" )
    # left and up diagonal 
    c  = c_q - 1
    r  = r_q + 1

    while True:

        if c < 1 or r > n:
            break

        p = [ r, c ]

        #print( p )

        if p in obstacles:

            #print( "{0} is inside".format( p ) )
            
            break

        res += 1

        c -= 1
        r += 1
    
    #print( "left and down" )
    # left and down diagonal 
    c  = c_q - 1
    r = r_q - 1
    while True:

        if c < 1 or r < 1:
            break

        p = [ r, c ]

        #print( p )

        if p in obstacles:

            #print( "{0} is inside".format( p ) )
            
            break

        res += 1

        c -= 1
        r -= 1

    #print( "right and down" )
    # right and down diagonal 
    c  = c_q + 1
    r  = r_q - 1

    while True:

        if c > n or r < 1:
            break

        p = [ r, c ]

        #print( p )

        if p in obstacles:

            #print( "{0} is inside".format( p ) )
            
            break

        res += 1

        c += 1
        r -= 1
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
