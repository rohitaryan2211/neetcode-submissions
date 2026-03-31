class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)):
            length = 0
            n = nums[i]
            while n in nums:
                length += 1
                n += 1
            res = max(res, length)
        return res