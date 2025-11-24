# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 22:29:09 2025

@author: suresh.burra
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        left = []
        right = []
        pivot = arr[0]
        for i in range(1, len(arr)):
            if arr[i]<=pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
                
    return quickSort(left) + [pivot] + quickSort(right)
        
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
