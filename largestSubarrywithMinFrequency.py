from collections import Counter, defaultdict

def findConsistentLogs(userEvent):
    n = len(userEvent)
    
    # Calculate the minimum frequency in the entire array
    total_count = Counter(userEvent)
    min_frequency = min(total_count.values())
    
    # Variables to keep track of the sliding window
    left = 0
    max_len = 0
    current_count = defaultdict(int)
    
    for right in range(n):
        current_count[userEvent[right]] += 1
        
        # While the max frequency in the current window is greater than min_frequency, move the left pointer
        while max(current_count.values()) > min_frequency:
            current_count[userEvent[left]] -= 1
            if current_count[userEvent[left]] == 0:
                del current_count[userEvent[left]]
            left += 1
        
        # Check if the current window is valid
        if max(current_count.values()) == min_frequency:
            max_len = max(max_len, right - left + 1)
    
    return max_len

# Example usage
userEvent = [1, 2, 1, 3, 4, 2, 4, 3, 3, 4]
print("Maximum length of consistent logs:", findConsistentLogs(userEvent))