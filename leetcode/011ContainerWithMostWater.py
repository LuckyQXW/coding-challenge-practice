"""
Given n non-negative integers a1, a2, ..., an , where each represents a
point at coordinate (i, ai). n vertical lines are drawn such that the two
endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution:
    def maxArea(self, height):
        """
        P:
        Brute force: try every combo i, j (j > i) and calculate the water it
        contains
        Area = min(height[i], height[j]) * (j - i)
        Runtime: O(N^2)
        Optimize: two pointer from outermost to inner most
        l = 0, r = len(height) - 1
        max_area = 0
        while r > l
        if arr[l] <= arr[r], l += 1
        if arr[r] > arr[j], r += 1
        take area = max(curr_area, max_area)
        Runtime: O(N)
        """
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        max_area = min(height[l], height[r]) * (r - l)
        while r > l:
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
        return max_area


"""
height = [1,8,6,2,5,4,8,3,7]
len = 9
l = 5
r = 6
max_area = max(49, 4) = 49
height[l] = 4
height[r] = 8
"""
