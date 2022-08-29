class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result=[sum(x) for x in accounts]
        result2=sorted(result, reverse=True)[0]
        return result2
      
# Runtime: 85 ms, faster than 51.89% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 13.9 MB, less than 32.44% of Python3 online submissions for Richest Customer Wealth.
