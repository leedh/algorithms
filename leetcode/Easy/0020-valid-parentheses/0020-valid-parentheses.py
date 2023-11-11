class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '{':'}', '[':']'}

        for c in s:
            if c in '({[': # open bracket
                stack.append(c) 
            elif len(stack) == 0 or c != brackets[stack.pop()]: # closing bracket
                return False
        return len(stack) == 0 # make sure that all brackets are removed in the stack
                    

