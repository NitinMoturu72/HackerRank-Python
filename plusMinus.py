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