#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.burra
#
# Created:     31-08-2025
# Copyright:   (c) suresh.burra 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys
# https://www.hackerrank.com/contests/executive-m-tech-test-3
#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    seen = {}
    for i, price in enumerate(arr):
        complement = m - price
        if complement in seen:
            # Return 1-based indices in ascending order
            return sorted([seen[complement] + 1, i + 1])
        seen[price] = i
    return []

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()