class Solution:
    def firstUniqChar(self, s: str) -> int:
        sMap = collections.Counter(s)
        
        for ind, ch in enumerate(s):
            print(ind, ch)
            if sMap[ch] == 1:
                return ind
        return -1
        
        