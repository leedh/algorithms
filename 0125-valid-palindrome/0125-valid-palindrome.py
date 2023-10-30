import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" " , "")
        for character in string.punctuation:
            s = s.replace(character, "")
        
        s_reverse = s[::-1]
        return s == s_reverse