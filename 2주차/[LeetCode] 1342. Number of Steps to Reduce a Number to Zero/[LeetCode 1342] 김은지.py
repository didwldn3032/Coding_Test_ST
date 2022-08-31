class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = num
        cnt = 0
        while res != 0:
            if res % 2 == 0:
                res /= 2
            else:
                res -= 1
            cnt += 1

        return cnt

'''
Runtime: 23 ms, faster than 99.57% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 13.9 MB, less than 52.70% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
'''