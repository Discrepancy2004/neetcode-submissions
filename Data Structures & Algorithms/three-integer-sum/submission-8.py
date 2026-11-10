from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Two pointer approach

        nums = sorted(nums)
        freq = Counter(nums)
        res = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while(l<r ):
                if l == i:
                    l = l + 1
                    
                elif r == i:
                    r = r - 1
                s = nums[l] + nums[r] + nums[i]
                if s== 0:
                    res.append([nums[l] , nums[r] , nums[i]])
                    l = l + 1
                    r = r -1

                    while(l<r and nums[l] == nums[l-1]):
                        l = l + 1
                    while(l<r and nums[r]==nums[r+1]):
                        r = r-1
                elif s<0:
                    l = l + 1
                elif s>0:
                    r = r - 1
                
        return res