class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                result.append("FizzBuzz")
            elif i%3==0:
                result.append("Fizz")
            elif i%5==0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result    

# Runtime: 41 ms, faster than 97.10% of Python3 online submissions for Fizz Buzz.
# Memory Usage: 15 MB, less than 85.47% of Python3 online submissions for Fizz Buzz.