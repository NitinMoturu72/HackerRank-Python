# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example
# 1 2 3 4 5

# The minimum sum is  and the maximum sum is . The function prints
# 16 24

# Function Description
# Complete the miniMaxSum function in the editor below.
# miniMaxSum has the following parameter(s):
# arr: an array of  integers

# Print
# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format
# A single line of five space-separated integers.

# Output Format
# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# (The output can be greater than a 32 bit integer.)

# Sample Input
# 1 2 3 4 5

# Sample Output
# 10 14

# Explanation

# The numbers are , , , , and . Calculate the following sums using four of the five integers:
# Sum everything except , the sum is .
# Sum everything except , the sum is .
# Sum everything except , the sum is .
# Sum everything except , the sum is .
# Sum everything except , the sum is .
# Hints: Beware of integer overflow! Use 64-bit Integer.


import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    minsum = arr[0]
    maxsum = arr[-1]
    for i in range(1,4):
        minsum += arr[i]
        maxsum += arr[-(i+1)]
    print(str(minsum) + " " + str(maxsum))


arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
