import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.num,self.k = nums,k
        heapq.heapify(self.num)
        while(len(nums) > k):
            heapq.heappop(self.num)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.num,val)
        if len(self.num) > self.k:
            heapq.heappop(self.num)
        return self.num[0]
        

