class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.total = 0
        cur = []
        res = []
        def dfs(i):
            if self.total == target:
                res.append(cur.copy())
                return
            if i>=len(nums) or self.total > target:
                return

            cur.append(nums[i])
            self.total += nums[i]
            dfs(i)
            n = cur.pop()
            self.total = self.total - n
            dfs(i+1)

        dfs(0)
        return res