class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max, left, right = 0, 0, len(heights) - 1

        while left < right:
            current_size = (right - left) * min(heights[left], heights[right])
            if curr_max < current_size:
                curr_max = current_size
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return curr_max