from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        path = set()
        hm = defaultdict(list)

        for e1,e2 in edges:
            hm[e1].append(e2)
            hm[e2].append(e1)

        def dfs(num):
            if num in path:
                return
            path.add(num)
            for i in hm[num]:
                dfs(i)

        count = 0
        for i in range(n):
            if i not in path:
                dfs(i)
                count = count + 1
        return count

