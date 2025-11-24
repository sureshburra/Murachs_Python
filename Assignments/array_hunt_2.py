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
    n = int(input().strip())
    arr = list(map(int, input().split()))
    x = int(input().strip())

    for i in range(n):
        if arr[i] == x:
            print(i)
            return

    print(-1)

if __name__ == "__main__":
    main()