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
n=int(input("Enter your choice "))

factorial = 1
if n <0:
    print(f"Factorial of given number {n} is not possible")
elif n==0 or n==1:
    print(f"The factorial of given number {n} is {1}")
else:
    for i in range(1,n+1):
        factorial = i * factorial
    print(f"The factorial of given number {n} is {factorial}")
