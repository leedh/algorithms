import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" " , "")
        for character in string.punctuation:
            s = s.replace(character, "")
        s_reverse = s[::-1]
        if s == s_reverse:
            return True
        else:
            return False
