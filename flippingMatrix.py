def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    max_ulq = 0
    for i in range(n):
        for j in range(n-1-i):
            max_element = max(matrix[i][j], matrix[n-1-i][j], matrix[i][n-1-j], matrix[n-1-i][n-1-j])
            max_ulq += max_element
    return max_ulq