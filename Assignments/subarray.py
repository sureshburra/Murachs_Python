import math
import os


def maxSubarray(arr):
    max_subarray_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_subarray_sum = max(max_subarray_sum, current_sum)

    max_subsequence_sum = 0
    all_negative = True
    max_element = arr[0]

    for num in arr:
        if num > 0:
            max_subsequence_sum += num
            all_negative = False
        max_element = max(max_element, num)

    if all_negative:
        max_subsequence_sum = max_element

    return [max_subarray_sum, max_subsequence_sum]


arr = [-9, -4, -2, 5, 7, 11]
values = maxSubarray(arr)
print(values)
