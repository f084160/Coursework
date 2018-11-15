def isPalindrome(S):
    """This function will determine if the input string will produce an 
    boolean output stating true if string is a palindrome false if not"""
    if len(S)<2:
        return True
    inputIndex = S[0]
    inputIndex2 = S[-1]
    if inputIndex != inputIndex2:
        return False
    else:
        innerInputIndex = S[1:-1]
        return isPalindrome(innerInputIndex)
