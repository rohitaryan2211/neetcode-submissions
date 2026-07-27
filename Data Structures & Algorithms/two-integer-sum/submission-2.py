class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            new_num = target - nums[i]
            if new_num in nums[i+1:]:
                return [i, i+1+nums[i+1:].index(new_num)]