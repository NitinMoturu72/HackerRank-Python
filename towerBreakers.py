# Two players are playing a game of Tower Breakers! Player  always moves first, and both players always play optimally.The rules of the game are as follows:

# Initially there are n towers.
# Each tower is of height m.
# The players move in alternating turns.
# In each turn, a player can choose a tower of height x and reduce its height to y, where (1 <= y < x) and y evenly x divides .
# If the current player is unable to make a move, they lose the game.
# Given the values of n and m, determine which player will win. If the first player wins, return 1. Otherwise, return 2.

# Example. 

# There are  towers, each  units tall. Player  has a choice of two moves:
# - remove  pieces from a tower to leave  as 
# - remove  pieces to leave 

# Let Player  remove . Now the towers are  and  units tall.

# Player  matches the move. Now the towers are both  units tall.

# Now Player  has only one move.

# Player  removes  pieces leaving . Towers are  and  units tall.
# Player  matches again. Towers are both  unit tall.

# Player  has no move and loses. Return .

# Function Description

# Complete the towerBreakers function in the editor below.

# towerBreakers has the following paramter(s):

# int n: the number of towers
# int m: the height of each tower
# Returns

# int: the winner of the game


def towerBreakers(n, m):
    # Write your code here
    count = 0 
    if (m == 1):
        return 2
    elif (n%2 == 0):
        return 2
    else:
        return 1
    
print(towerBreakers(1,2))