class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [''] * n
        for i in range(n):
            if (i + 1) % 3 == 0:
                res[i] += "Fizz"
            if (i + 1) % 5 == 0:
                res[i] += "Buzz"
            elif (i + 1) % 3 != 0 and (i + 1) % 5 != 0:
                res[i] += str(i + 1)

        return res

'''
Runtime: 80 ms, faster than 23.20% of Python3 online submissions for Fizz Buzz.
Memory Usage: 15.3 MB, less than 5.13% of Python3 online submissions for Fizz Buzz.
'''