class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        maxArea = 0
        area = 0
        while (l<r):
            area = min(heights[l],heights[r]) * (r-l)
            maxArea = max(maxArea,area)
            print(area)

            if heights[l] > heights[r]:
                r = r-1
            else:
                l = l + 1
        
        return maxArea

