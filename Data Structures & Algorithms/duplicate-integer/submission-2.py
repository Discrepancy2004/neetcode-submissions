from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1

        for num in nums:
            if hm[num] > 1:
                return True
        
        return False