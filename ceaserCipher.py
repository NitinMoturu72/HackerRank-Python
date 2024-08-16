# Julius Caesar protected his confidential information by encrypting it using a cipher. 
# Caesar's cipher shifts each letter by a number of letters. 
# If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
# In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Example
# s = 'ABCD'
# k = 3

# Cipher : 'DEFG'

# The alphabet is rotated by k, matching the mapping above.

# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

# Function Description

# Complete the caesarCipher function in the editor below.
# caesarCipher has the following parameter(s):

# string s: cleartext
# int k: the alphabet rotation factor

# Returns
# string: the encrypted string

# Input Format

# The first line contains the integer, , the length of the unencrypted string.
# The second line contains the unencrypted string, .
# The third line contains , the number of letters to rotate the alphabet by.

def caesarCipher(s, k):
    # Write your code here
    # print(s)
    cipher = ""
    k = k % 26
    for i in s:
        num = ord(i)
        if (num > 64 and num< 91):
            cnum = num + k
            if (cnum>90):
                cnum = (cnum-90) + 64
            cipher += chr(cnum)
        elif(num > 96 and num < 123):
            cnum = num + k
            if (cnum>122):
                cnum = (cnum-122) + 96
            cipher += chr(cnum)
        else:
            cipher += i
    return cipher

print(caesarCipher("ABCD",35))