from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for word in strs:
            s = tuple(sorted(word))
            
            hm[s].append(word)
            
        return list(hm.values())