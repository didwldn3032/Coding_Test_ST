class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [sum(l) for l in mat]
        sorted_soldiers = list(set(sorted(soldiers)[:k]))
        res = []

        while len(res) < k:
            for r in sorted_soldiers:
                res.extend(list(filter(lambda x: soldiers[x] == r, range(len(soldiers)))))
            if len(res) > k:
                res = res[:k]

        return res

'''
Runtime: 136 ms, faster than 77.42% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 14.3 MB, less than 13.91% of Python3 online submissions for The K Weakest Rows in a Matrix.
'''