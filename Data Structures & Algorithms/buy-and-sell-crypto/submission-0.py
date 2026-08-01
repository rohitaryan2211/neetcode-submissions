class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(len(prices)-1):
            res = max(res, max(prices[i+1:])-prices[i])
            # print(res, max(prices[i+1:]), prices[i])

        return res