class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack.pop() != mapping[char]:
                    return False
        return len(stack) == 0

        # if len(stack)==0:
        #     return true
        # else:
        #     return false

#if not stack or stack.pop() != mapping[char]
    #interpretation: two conditions, 1. not stack checks whether the stack is 
    #already empty, 2. whether the element popped from the stack matches the char 
    #in the position of char in the dic mapping 