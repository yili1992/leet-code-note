class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        d_0_0_left = 0
        d_0_1_left = - prices[0]
        d_0_0 = 0
        d_0_1 = 0
        for i in range(1, length):
            d_0_0 = max(d_0_0_left, d_0_1_left + prices[i])
            d_0_1 = max(d_0_1_left, d_0_0_left - prices[i])
            d_0_1_left = d_0_1
            d_0_0_left = d_0_0
        return d_0_0


s = Solution()
price =[7,1,5,3,6,4]
print(s.maxProfit(price))