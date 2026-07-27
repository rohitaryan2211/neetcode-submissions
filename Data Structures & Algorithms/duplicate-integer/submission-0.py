class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []
        for x in nums:
            if x in res:
                return True
            else:
                res.append(x)
        return False