class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy first, then sell - buy low, sell high

        #sliding window - left to track buy day
        #right to track sell day - and if right<left, left=right
        #if right > left - update max
        res = 0
        l = 0 
        for r in range(1, len(prices)):
            maxprofit = prices[r]-prices[l]
            if prices[r] < prices[l]:
                l = r
            else:
                res = max(res, maxprofit)
        return res















        # res = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         res = max(res, sell - buy)
        # return res