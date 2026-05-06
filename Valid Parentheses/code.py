class Solution:
    def isValid(self, s: str) -> bool:
        # define the dict
        brackets = {")":"(", "]":"[", "}":"{"}

        # iterate through with a stack
        stack = []
        for brac in s:
            if brac in brackets and stack:
                if brackets[brac] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(brac)
        return not stack
            
        

        