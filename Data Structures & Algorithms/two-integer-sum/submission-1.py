from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(int)
        res = []
        for i,num in enumerate(nums):
            comp = target - num
            if comp in hm:
                res.append(hm[comp])
                res.append(i)
                break
            
            hm[num] = i
        
        return res
