class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs  = set() 
        for num in nums:
            hs.add(num)

        
        maxCount = 0

        for num in hs:
            if num - 1 not in hs:
                count = 1

                while num + 1 in hs:
                    count += 1
                    num += 1

            

                maxCount = max(maxCount,count)
        
        return maxCount