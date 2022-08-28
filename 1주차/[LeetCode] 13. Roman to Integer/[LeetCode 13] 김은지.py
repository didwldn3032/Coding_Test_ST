class Solution:
    def romanToInt(self, s: str) -> int:
        sv_pairs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res, i = 0, 0
        s = list(s)  # list로 변환

        while 1:
            if i == len(s):
                return res
            elif i == len(s) - 1:
                res += sv_pairs[s[i]]
            elif sv_pairs[s[i]] < sv_pairs[s[i + 1]]:
                res += sv_pairs[s[i + 1]] - sv_pairs[s[i]]
                i += 1
            else:
                res += sv_pairs[s[i]]
            i += 1

