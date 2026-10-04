import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        arr = []
        for coords in points:
            distance = (coords[0] ** 2)+(coords[1] ** 2)
            
            arr.append((distance,coords))
        heapq.heapify(arr)
        count = 0
        res = []
        while(count != k) :
            distance,coords = heapq.heappop(arr)
            res.append(coords)
            count = count + 1
        
        return res


        
