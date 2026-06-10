class Solution:
    # Time complexity: O(n).
    # Space complexity: O(n).
    def isValid(self, s: str) -> bool:
        '''Requirements for validity:
            - same type: hashmap
            - correct order: closing parenthesis always matches the most recent closing one (stack)
        '''
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # we can add open parenthesis as many as we want
        
        return True if not stack else False

        