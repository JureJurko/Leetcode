class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append((temperature, i))
        return result
            


