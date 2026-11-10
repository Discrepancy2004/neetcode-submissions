from collections import Counter
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        hm = {}
        res = set()
        freq = Counter(nums)
        for i in range(n):
            for j in range(i + 1,n):
                valid = True
                target = -nums[i]-nums[j]
                if target not in freq:
                    continue
                
                need = Counter([nums[i],nums[j],target])
                for item in need.items():
                    if freq[item[0]] < item[1]:
                        valid = False
                    
                if valid:
                    res.add(tuple(sorted([nums[i],nums[j],target])))
        res1 = [] 
        for nums in res:
            res1.append(list(nums))
        return res1
                    