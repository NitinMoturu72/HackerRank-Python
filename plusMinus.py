# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Example
# arr = [1,1,0,-1,-1]
# There are  elements, two positive, two negative and one zero. Their ratios are 0.400000, 0.400000 and 0.200000 Results are printed as:
# 0.400000
# 0.400000
# 0.200000
# Function Description

# Complete the plusMinus function in the editor below.

# plusMinus has the following parameter(s):

# int arr[n]: an array of integers
# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. 
# The function should not return a value.

# Input Format

# The first line contains an integer, , the size of the array.
# The second line contains  space-separated integers that describe .

# Output Format

# Print the following  lines, each to  decimals:

# proportion of positive values
# proportion of negative values
# proportion of zeros


import math
import os
import random
import re
import sys
import decimal


def plusMinus(arr):
    # Write your code here
    countp = decimal.Decimal(0.000000)
    countn = decimal.Decimal(0.000000)
    countz = decimal.Decimal(0.000000)
    length = decimal.Decimal(len(arr))
    # print(length)
    for i in arr:
        # print(i)
        if (i > 0):
            countp += 1
        elif (i < 0):
            countn += 1
        else:
            countz += 1
    
    print(round((countp/length),6))
    print(round((countn/length),6))
    print(round((countz/length),6))


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)