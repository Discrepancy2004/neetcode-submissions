class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [float('inf')] * n
        arr[n-1] = 0

        for i in range(n-2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    arr[i] = min(arr[i], 1 + arr[i+j])
            
        return arr[0]