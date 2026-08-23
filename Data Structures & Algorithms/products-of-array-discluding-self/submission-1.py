class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_0 = nums.count(0)
        res = []
        if count_0 == 0:
            prod = 1
            for x in nums:
                prod *= x
            for x in nums:
                res.append(int(prod/x))
        elif count_0 == 1:
            prod = 1
            for x in nums:
                if x != 0:
                    prod *= x
            for x in nums:
                if x == 0:
                    res.append(prod)
                else:
                    res.append(0)
        else:
            for x in nums:
                res.append(0)
        return res