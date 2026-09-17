class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        res = []
        
        l = 0
        r = n -1 
            
        while(l<r):
            if numbers[l] + numbers[r] == target:
                res = [l+1,r+1]
                break
                
            elif numbers[l] + numbers[r] > target:
                r = r-1
                
            elif numbers[l] + numbers[r] < target:
                l = l + 1
        
        return res