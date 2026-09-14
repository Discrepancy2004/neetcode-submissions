from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = []
        res = []
        for i in range(len(nums) + 1):
            buckets.append([])
        
        for num,count in freq.items():
            buckets[count].append(num)
        
        for i in range(len(nums),-1,-1):
            for j in buckets[i]:
                res.append(j)
            
            if len(res) == k:
                break
        return res
