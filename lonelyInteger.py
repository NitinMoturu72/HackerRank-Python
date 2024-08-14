# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example
# a =[1,2,3,4,3,2,1]
# The unique element is 4.

# Function Description

# Complete the lonelyinteger function in the editor below.

# lonelyinteger has the following parameter(s):
# int a[n]: an array of integers

# Returns
# int: the element that occurs only once

# Input Format
# The first line contains a single integer, , the number of integers in the array.
# The second line contains  space-separated integers that describe the values in .

# Constraints

# It is guaranteed that  is an odd number and that there is one unique element.



def lonelyinteger(a):
    # Write your code here
    seen = []
    for i in a:
        if i not in seen:
            seen.append(i)
        elif i in seen:
            seen.remove(i)
    return seen[0]

n = input()
a = list(map(int, input().rstrip().split()))
print(lonelyinteger(a))