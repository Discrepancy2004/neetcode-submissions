class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hs = set()
        
        maxLen = 0
        for r in range(len(s)):
            if s[r] in hs:
                while s[r] in hs:
                    hs.remove(s[l])
                    l += 1
            
            hs.add(s[r])
            maxLen = max(maxLen,r-l+1)

        return maxLen

    

