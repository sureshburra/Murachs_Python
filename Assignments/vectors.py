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
import numpy as np

# Create vectors
v1=np.array([1,2,3])
v2=np.array([4,5,6])

print(f"Vector 1 is : {v1}")
print(f"Vector 2 is : {v2}")

print(f"The addition of two vectors is : {v1+v2}")
print(f"Element wise multiplication of two vectors is : {v1*v2}")
print(f"Element wise division of two vectors is : {v1/v2}")
print(f"Add any scalar in Vector : {3+v1}")
print(f"Multiplication of any scalar in Vector : {3*v1}")
print(f"Dot product of any two vectors is : {np.dot(v1,v2)}")
print(f"Cross product of two vectors is :{np.cross(v1,v2)}")

v = np.array([1,2,3])
minima = np.min(v1)
maxima = np.max(v1)
mean = np.mean(v1)
median = np.median(v1)
variance = np.var(v1)

print(f"Minima of given array is {minima}")



mylist = [1,4,50]

for i in range(0, len(mylist)):
    print(mylist[i])

# Find Minimal number

# Prime numbers

