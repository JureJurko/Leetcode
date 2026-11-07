import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }
        stack = []
        result = 0

        for token in tokens:
            if token in operators:
                result = operators.get(token)(stack.pop(-2), stack.pop())
                stack.append(result)
                continue
            
            stack.append(int(token))
        
        return stack.pop()
