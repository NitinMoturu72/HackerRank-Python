def gridChallenge(grid):
    # Write your code here
    ngrid = []
    for i in grid:
        temp = ''.join(sorted(i))
        ngrid.append(temp)
    print(ngrid)
    
    for i in range(len(ngrid[0])):
        for j in range(len(ngrid)-1):
            if (ngrid[j][i]>ngrid[j+1][i]):
                return 'NO'
    return "YES"


print(gridChallenge(['abc', 'ade', 'efg']))