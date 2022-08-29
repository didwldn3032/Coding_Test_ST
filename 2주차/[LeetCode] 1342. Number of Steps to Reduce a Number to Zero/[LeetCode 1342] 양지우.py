class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while True:
            if num==0:
                break
            if num%2==0:
                num=num/2
            else:
                num-=1
            count+=1
        return count

# Runtime: 38 ms, faster than 79.08% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.8 MB, less than 52.73% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
