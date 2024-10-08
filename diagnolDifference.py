# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:
# 1 2 3
# 4 5 6
# 9 8 9  

# The left-to-right diagonal = 15.
# The right to left diagonal = 17.
# Their absolute difference is 2.

# Function description
# Complete the  function in the editor below.

# diagonalDifference takes the following parameter:
# int arr[n][m]: an array of integers
# Return
# int: the absolute diagonal difference

# Input Format
# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .

# Output Format
# Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

# Sample Input
# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# Sample Output
# 15

# Explanation

# The primary diagonal is:
# 11
#    5
#      -12
# Sum across the primary diagonal: 11 + 5 - 12 = 4

# The secondary diagonal is:
#      4
#    5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19

# Difference: |4 - 19| = 15


def diagonalDifference(arr):
    # Write your code here
    ldiag = 0
    rdiag = 0
    length = len(arr)
    for i in range(length):
        for j in range(length):
            if (i == j):
                ldiag += arr[i][j]
            if (i+j == length-1):
                rdiag += arr[i][j]
    return abs(ldiag-rdiag)


n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(result)
