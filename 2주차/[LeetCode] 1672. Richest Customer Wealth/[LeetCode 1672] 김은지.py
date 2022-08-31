class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(accounts[r]) for r in range(len(accounts))])


'''
Runtime: 63 ms, faster than 83.49% of Python3 online submissions for Richest Customer Wealth.
Memory Usage: 13.9 MB, less than 32.34% of Python3 online submissions for Richest Customer Wealth.
'''