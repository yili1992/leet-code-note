class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        length = len(prices)
        d_i_left = 0
        d_i = 0
        min_value = prices[0]
        for i in range(1, length):
            d_i = max(d_i_left, prices[i] - min_value)
            min_value = min(prices[i], min_value)
            d_i_left = d_i
        return d_i




s = Solution()
price =[7,1,5,3,6,4]
print(s.maxProfit(price))