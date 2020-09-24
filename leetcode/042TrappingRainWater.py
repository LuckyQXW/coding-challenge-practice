"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.
"""


class Solution:
    def trap(self, height):
        """
        P:
        Two pointers
        Keep track of left, right, left_max, right_max
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        if left_max < right_max:
            ans += left_max - height[left]
            left += 1
        else:
            ans += right_max - height[right]
            right -= 1
        """
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        ans = 0
        while right > left:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
