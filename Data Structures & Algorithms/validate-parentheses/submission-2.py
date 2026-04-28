class Solution:
    def isValid(self, s: str) -> bool:

        pair = {"{": "}", "[": "]", "(": ")"}
        stack = []

        # s = [,(

        for char in s:
            if char in pair:
                stack.append(char)
            else:
                if not stack or pair[stack.pop()]!= char:
                    return False
        
        return len(stack) == 0
                
        