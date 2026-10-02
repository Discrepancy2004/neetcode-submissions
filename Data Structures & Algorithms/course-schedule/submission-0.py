from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = defaultdict(list)
        for crs,pre in (prerequisites):
            hm[crs].append(pre)
        path = set()
        def dfs(crs):
            if crs in path:
                return False
            
            if hm[crs] == []:
                return True

            path.add(crs)

            for pre in hm[crs]:
                if dfs(pre) == False:
                    return False

            path.remove(crs)
            hm[crs] = []
            return True
        for crs in list(hm.keys()):
            if dfs(crs) == False:
                return False
        return True
            

