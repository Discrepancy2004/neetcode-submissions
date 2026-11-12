class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(list(s)))
        t = ''.join(sorted(list(t)))
       

        if (s == t):
            return True
        else:
            return False