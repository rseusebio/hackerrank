#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def qnt_inside(arr: List[int], s: int , t: int, d: int) -> int:
    qnt = 0
    for e in arr:
        x = d + e 
        if s <= x and x <= t:
            qnt += 1
    return qnt

def countApplesAndOranges(s, t, a, b, apples, oranges):
    qnt_apples = qnt_inside(apples, s, t, a)
    qnt_oranges = qnt_inside(oranges, s, t, b)
    
    
    print(qnt_apples)
    print(qnt_oranges)
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
