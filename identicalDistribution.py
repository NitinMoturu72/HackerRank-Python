# Identical Distribution

# An e-commerce company specializes in cards with sports figures on them. Each sport has different categories of cards. 
# For instance, there might be more desirable cards with the most popular sports personalities, others with small pieces of a player's jersey attached, and so on. 
# They have a number of each category of card and want to make some number of packets greater than 1 that each contain equal numbers of each type of card. 
# To do this, they will add more cards of each type until each type can be divided equally among some number of packets. 
# Determine the minimum number of additional cards needed to create a number of packets with equal type distribution.

# Example 
# n=5
# cardTypes = [4, 7, 5, 11, 15)
# In order to make 2 matching packets, the following numbers of additional cards of each type must be added: [0, 1, 1, 1, 1]. 
# This sums to 4 additional cards. The numbers of cards are [4, 8, 6, 12, 16] and they can be divided evenly among 2 packets. 
# 
# If 3 packets are created, an additional [2, 2, 1, 1, 0] cards are needed, sum = 6 items. 
# This yields quantities [6, 9, 6, 12, 15]. Any number of packets ≥ 2 can be created, but creating 2 packets requires the minimum number of additional cards.

# Function Description
# Complete the function cardPackets in the editor below.
# cardPackets has the following parameter(s):
# int cardTypes[n]: the quantity available of card type
# Returns
# int: the minimum number of additional cards to add


def distribute(arr):
    count2 = 0
    count3 = 0
    count5 = 0
    for i in arr:
        if (i%2 != 0):
            count2 += (i%2)
        
        if (i%3 != 0):
            count3 += (3-(i%3))

        if (i%5 != 0):
            count5 += (5-(i%5))

    return min(count2, count3, count5)
    
print(distribute([5,10,15,20]))