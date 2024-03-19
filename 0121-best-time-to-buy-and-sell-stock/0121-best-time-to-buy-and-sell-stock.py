class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=-sys.maxsize
        buy=+sys.maxsize
        for i in range(len(prices)):
            buy=min(buy,prices[i])
            mx=max(mx,prices[i]-buy)
        return mx