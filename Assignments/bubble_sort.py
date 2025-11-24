# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 11:59:55 2025

@author: suresh.burra
"""

def countSwaps(arr):
    n = len(arr)
    numSwaps = 0
    
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j + 1],arr[j]
                numSwaps += 1
        
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {arr[0]}")
    print(f"Last Element: {arr[-1]}")

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)