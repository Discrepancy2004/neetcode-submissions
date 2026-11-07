class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        n = len(nums)
        for num in range(1,n):
            if currSum < 0:
                currSum = 0
            currSum += nums[num]    
            maxSum = max(maxSum,currSum)
        return maxSum
            
