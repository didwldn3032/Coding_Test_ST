class Solution:
    def romanToInt(self, s:str) ->int:
        input_list=list(s)
        Rtol={'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}
        result=list(map(lambda x:Rtol[x],input_list))
        for i in range(len(result)-1):
            if result[i]<result[i+1]:
                result[i+1]-=result[i]
                result[i]=0
        return sum(list(result))

# Runtime: 55 ms, faster than 85.37% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14 MB, less than 31.05% of Python3 online submissions for Roman to Integer.