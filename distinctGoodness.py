def getDistinctGoodnessValues(arr):
    n = len(arr)
    goodness_set = set()

    # Initialize the goodness_set with 0 for the empty subsequence
    goodness_set.add(0)

    for num in arr:
        # Create a temporary set to store new goodness values
        new_goodness = set()
        for g in goodness_set:
            # Calculate the new goodness by OR-ing with the current number
            new_goodness.add(g | num)
            print(new_goodness, g, num)
        
        # Add all new goodness values to the main set
        goodness_set.update(new_goodness)

    # Convert the set to a sorted list
    return sorted(list(goodness_set))

# Example usage:
arr = [3,2,4,6]
print(getDistinctGoodnessValues(arr))