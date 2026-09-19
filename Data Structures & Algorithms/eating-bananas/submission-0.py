class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mid = 0
        k = 0
        while(l<r):
            mid = l + (r - l)//2
            k= 0
            for bananas in piles:
                rate = bananas//mid 
                if bananas % mid != 0:
                    rate = rate + 1
                k += rate

            if k > h:
                l = mid + 1
            else:
                r = mid

        return r
            