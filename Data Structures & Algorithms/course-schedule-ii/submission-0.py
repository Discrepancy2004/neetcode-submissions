from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = defaultdict(list)
        self.res = []

        for crs, pre in prerequisites:
            hm[crs].append(pre)

        path = set()
        done = set()

        def dfs(crs):
            if crs in path:
                self.res = []
                return False

            if crs in done:
                return True

            if hm[crs] == []:
                self.res.append(crs)
                done.add(crs)
                return True

            path.add(crs)

            for pre in hm[crs]:
                if not dfs(pre):
                    return False

            path.remove(crs)
            hm[crs] = []
            done.add(crs)
            self.res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return self.res