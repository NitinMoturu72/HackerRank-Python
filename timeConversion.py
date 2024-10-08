# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note:- 
# 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example
# s = '12:01:00PM'
# Return '12:01:00'.

# s = '12:01:00AM'
# Return '00:01:00'.

# Function Description
# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):
# string s: a time in  hour format

# Returns
# string: the time in  hour format

# Input Format
# A single string  that represents a time in -hour clock format (i.e.:  or ).

# All input times are valid

# Sample Input
# 07:05:45PM

# Sample Output
# 19:05:45



def timeConversion(s):
    # Write your code here
    period = s[-2:]
    hour = int(s[:2])
    minsec = s[2:8]
    # print(minsec)
    if (period == "PM" and hour>0 and hour<12):
        hour += 12
    elif (period == "AM" and hour == 12):
        hour = 0
    
    if (hour<12):
        time = "0"+str(hour)+minsec
    else:
        time = str(hour)+minsec
    
    print(time)
    return time

s = input()
result = timeConversion(s)