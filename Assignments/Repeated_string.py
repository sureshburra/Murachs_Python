# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 07:51:34 2025

@author: suresh.burra
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    count_a = s.count('a')
    no_of_repetitions = n//len(s)
    reminder = n % len(s)
    count_in_reminder = s[:reminder].count('a')
    total = no_of_repetitions * count_a + count_in_reminder
    return total
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

