class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1=Counter(list(ransomNote))
        c2=Counter(list(magazine))
        for i in c1.keys():
            try:
                if c1[i]>c2[i]:
                    result=False
                    break
                else:
                    result=True
            except:
                result=False
        return result

# Runtime: 76 ms, faster than 69.64% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.5 MB, less than 6.00% of Python3 online submissions for Ransom Note.