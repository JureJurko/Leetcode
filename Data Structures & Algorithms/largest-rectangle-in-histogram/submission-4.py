class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            curr = i
            while stack and stack[-1][0] > height:
                curr_height, curr_index = stack.pop()
                max_area = max(max_area, (curr - curr_index) * curr_height)
                i = curr_index
            stack.append((height, i))
        

        for height, idx in stack:
            max_area = max(max_area, (len(heights) - idx) * height)

        return max_area

            