class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1 or len(prices) == 0:
            return 0
        minNum = 39999999999
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minNum:
                minNum = prices[i]
            elif prices[i] - minNum > profit:
                profit = prices[i] - minNum
        return profit 
            