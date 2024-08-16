


def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)
    sumulq = 0
    for i in range(n//2):
        for j in range(n//2):
            # print(matrix[i][j], i, j)
            # print(max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1]))
            sumulq += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
            
    return sumulq

print(flippingMatrix([[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]))