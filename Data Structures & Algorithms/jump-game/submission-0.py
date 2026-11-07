class Solution:
    def canJump(self, nums: List[int]) -> bool:
        leap = 0
        maxleap = 0

        for i,num in enumerate(nums):
            leap = num + i
            if maxleap<i:
                return False
            maxleap = max(maxleap,leap)
            print(i,maxleap,leap)

        return True
