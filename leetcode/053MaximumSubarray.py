import sys


# Brute force approach, O(n^3)
def maxSubArray(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        n = len(nums)
        max_sum = -sys.maxsize
        # Try every combo of i, j, then add up the sum between [i, j)
        for i in range(n):
            for j in range(i, n + 1):
                sum = nums[i]
                for k in range(i + 1, j):
                    sum += nums[k]
                    max_sum = max(sum, max_sum)
        return max_sum


# Optimize using prefix sum, O(n^2)
def maxSubArray1(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        n = len(nums)
        max_sum = -sys.maxsize
        # Only calculate prefix sums starting at every i, so no need to
        # go back and recalculate the sum from previous
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                max_sum = max(max_sum, sum)


# Further optimization, use current sum - previous min sum to get current max
def maxSubArray2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        n = len(nums)
        max_sum = nums[0]
        min_sum = 0
        sum = 0
        # Key observation: the max sum comes from
        # current prefix sum - previous min prefix sum
        for i in range(n):
            sum += nums[i]
            max_sum = max(max_sum, sum - min_sum)
            min_sum = min(min_sum, sum)
        return max_sum


"""
Test cases:
[]
[0]
[-1] - test negative
[1, 0, -1] - 1, normal case
[-2, -1]
[0, 1, -2, -1, 4, 2] - 6, max sum comes after
[1, 1, 1, 3, 2, -2, 5, 0] - 8, max sum comes before and not include max val
[2, 4, -2, 5, 0] - 7, max sum sequence contains negative
"""
