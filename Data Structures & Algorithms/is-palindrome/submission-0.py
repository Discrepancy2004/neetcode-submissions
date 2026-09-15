class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        res = ""
        for ch in t:
            if not ch.isalnum():
                continue
            res = res + ch
        return res == res[::-1]