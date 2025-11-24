#-------------------------------------------------------------------------------
# Name:        journeyToMoon
# Purpose:
#
# Author:      suresh.burra
#
# Created:     23-11-2025
# Copyright:   (c) suresh.burra 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/bin/python3

""" Problem statement:
    The member states of the UN are planning to send

people to the moon. They want them to be from different countries. You will be given a list of pairs of astronaut ID's. Each pair is made of astronauts from the same country. Determine how many pairs of astronauts from different countries they can choose from.

Example
n=4
atronaut=[1,2][2,3]

There are 4 astronauts numbered 0 through 3. Astronauts grouped by country are [0] and [1,2,3]. There are 3 pairs to choose from: [0,1],[0,2] and [0,3].



Function Description

Complete the journeyToMoon function in the editor below.

journeyToMoon has the following parameter(s):

    int n: the number of astronauts
    int astronaut[p][2]: each element

is a 2

    element array that represents the ID's of two astronauts from the same country

Returns
- int: the number of valid pairs

Input Format

The first line contains two integers
and , the number of astronauts and the number of pairs.
Each of the next lines contains

space-separated integers denoting astronaut ID's of two who share the same nationality.

Constraints
- 1<=n<=10^5
- 1<=p<=10^4


Sample Input 0

5 3
0 1
2 3
0 4

Sample Output 0

6

Explanation 0

Persons numbered [0,1,4]
belong to one country, and those numbered [2,3] belong to another. The UN has 6

ways of choosing a pair:
[0,2],[0,3],[1,2],[1,3],[4,2],[4,3]
Sample Input 1

4 1
0 2

Sample Output 1

5

Explanation 1

Persons numbered [0,2]
belong to the same country, but persons and don't share countries with anyone else. The UN has ways of choosing a pair:
[0,1],[0,3],[1,2],[1,3],[2,3]

"""

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    parent = list(range(n))
    size = [1] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if size[root_x] < size[root_y]:
                parent[root_x] = root_y
                size[root_y] += size[root_x]
            else:
                parent[root_y] = root_x
                size[root_x] += size[root_y]


    for a, b in astronaut:
        union(a, b)


    components = {}
    for i in range(n):
        root = find(i)
        components[root] = components.get(root, 0) + 1


    total_pairs = n * (n - 1) // 2


    same_country_pairs = 0
    for count in components.values():
        if count > 1:
            same_country_pairs += count * (count - 1) // 2

    return total_pairs - same_country_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

