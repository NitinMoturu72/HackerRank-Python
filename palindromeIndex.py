def palindromeIndex(s):
    # Write your code here
    index = -1
    if (checkPalindrome(s)):
        return index
    else:
        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            print(temp)
            if (checkPalindrome(temp)):
                return i
    return index

def checkPalindrome(s):
    st = 0
    ed = len(s)-1
    while (st< ed):
        if(s[st] != s[ed]):
            return False
        st += 1
        ed -= 1
    return True
        
    

print(palindromeIndex("prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp"))