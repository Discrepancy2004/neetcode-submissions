class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.total = 0
        cur = []
        res  = []
        candidates = sorted(candidates)
        def dfs(i):
            if self.total == target:
                res.append(cur.copy())
                return
            
            if i>=len(candidates) or self.total > target:
                return

            cur.append(candidates[i])
            self.total += candidates[i]
            dfs(i+1)
            n = cur.pop()

            while i<len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i = i+1
            self.total -= n

            dfs(i+1)

        dfs(0)
        return res