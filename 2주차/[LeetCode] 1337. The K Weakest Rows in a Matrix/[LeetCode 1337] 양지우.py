class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[]
        for i in range(len(mat)):
            ans.append((i,sum(mat[i])))
        f = sorted(ans, key = lambda x : x[1])
        result=[x[0] for x in f[:k]]
        return result
      
# Runtime: 131 ms, faster than 80.84% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.2 MB, less than 52.19% of Python3 online submissions for The K Weakest Rows in a Matrix.
