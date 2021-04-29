#!/bin/python3
import math
import os
import random
import re
import sys

def get_tradable_balls(container):
    t = 0
    
    for i in range(len(container)):
        t += container[i]

    return t

def get_balls_from_type(btype, M):
    t = 0

    for i in range(len(M)):    
        t += M[i][btype]
    
    return t

def organizingContainers(M):
    for i in range(len(M)):
        container = M[i]

        tradable_balls = get_tradable_balls(container[i+1:len(container)])
        
        total = get_balls_from_type(i, M[i+1:len(M)])

        print("index: {0}, remaining: {1}, total: {2}".format(i, tradable_balls, total))

        if tradable_balls != total:
            return "Impossible"

    return "Possible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries = int(input())

    for q in range(queries):
        n = int(input())

        M = []

        for _ in range(n):
            M.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(M)

        fptr.write(result + '\n')

    fptr.close()

# URL: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem