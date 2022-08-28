class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = 0
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, '', 1)
                cnt += 1
        return cnt == len(ransomNote)


'''
Runtime: 92 ms, faster than 47.64% of Python3 online submissions for Ransom Note.
Memory Usage: 14.2 MB, less than 53.15% of Python3 online submissions for Ransom Note.
'''