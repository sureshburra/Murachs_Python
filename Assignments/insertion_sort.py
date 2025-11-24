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

def main():
    N = int(input().strip())
    arr = list(map(int, input().split()))

    for i in range(1, N):
        key = arr[i]
        j = i - 1

        while j>=0 and arr[j]> key:
            arr[j+1] = arr[j]
            j= j -1
        arr[j+1] = key

    for i in range(0,N):
        print(arr[i],end=" ")


if __name__ == '__main__':
    main()
