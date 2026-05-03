class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif stack[-1] == '(' and char == ')':
                stack.pop()
            elif stack[-1] == '[' and char == ']':
                stack.pop()
            elif stack[-1] == '{' and char == '}':
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0

