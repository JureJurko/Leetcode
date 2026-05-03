# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            m1 = left + (right - left) // 3
            m2 = right - (right - left) // 3

            if guess(m1) == 0:
                return m1
            if guess(m2) == 0:
                return m2
            if guess(m1) + guess(m2) == 0:
                left = m1 + 1
                right = m2 - 1
            if guess(m1) < 0:
                right = m1 - 1
            if guess(m2) > 0:
                left = m2 + 1