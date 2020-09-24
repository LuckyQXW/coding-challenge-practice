class Solution:
    def fourSum(self, nums, target):
        """
        Brute force:
        Try every combination and check whether sum == target
        O(N^4) very inefficient
        Optimize:
        Set storing values seen
        i in range(0, len-2):
            j in range(i+1, len-1):
                k in range(j+1, len-0):
                    sum = nums[i] + nums[j] + nums[k]
                    check if target - sum in hash set
                    if not, store nums[i] in set
                    else add tuple(sorted[nums[i], nums[j], nums[k], target - sum]) to set
        O(N^3) is the best case runtime
        O(N) space necessary
        """
        seen = set()
        result = set()
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    total = nums[i] + nums[j] + nums[k]
                    if target - total in seen:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k], target - total])))
            seen.add(nums[i])
        list_result = [list(item) for item in result]
        return list_result

        """
        [1, 0, -1, 0, -2, 2]
         0  1  2   3  4   5
        seen = {1, 0, -1}
        result = {(-1, 0, 0, 1), (-2, -1, 1, 2), (-2, 0, 0, 2)}
        target = 0
        i = 4
        total = 0 + -2 + 2 = 0

        [0, 0, 0, 0, 0]
         0  1  2  3  4
        seen = {0}
        result = {(0, 0, 0, 0)}
        target = 0
        i = 1
        j = 2
        k = 4
        total = 0

        [0, 0, 0]
        seen = {0}
        result{}
        target = 0
        i = 1
        j = 2
        k = 3
        """


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.k_sum(nums, 4, target)

    def k_sum(self, nums, k, target):
        n = len(nums)
        # Empty result
        if k > n or self.get_sum(nums, 0, k) > target or self.get_sum(nums, n - k, n) < target:
            return []
        if k == 2:
            return self.two_sum(nums, target)
        else:
            result = []
            for i in range(n - k + 1):
                # list of unique elements adding up to target, need to make
                # sure i is not a duplicate from before to produce unique combos
                if i == 0 or nums[i-1] != nums[i]:
                    temp = self.k_sum(nums[i+1:], k - 1, target - nums[i])
                    for item in temp:
                        item.append(nums[i])
                        result.append(item)
            return result

    def get_sum(self, nums, start, end):
        """
        returns the sum from index start to end (exclusive) in nums
        """
        total = 0
        for i in range(start, end):
            total += nums[i]
        return total

    def two_sum(self, nums, target):
        """
        Use two pointer approach, skip duplicates
        """
        lo = 0
        hi = len(nums) - 1
        result = []
        while lo < hi:
            # Need to take into account the initial iteration
            if (lo > 1 and nums[lo] == nums[lo - 1]) or nums[lo] + nums[hi] < target:
                lo += 1
            elif (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]) or nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                result.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return result
