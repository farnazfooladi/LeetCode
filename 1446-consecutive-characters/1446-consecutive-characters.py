class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        prev = None
        max_count = 0
        for i in s:
            if i == prev:
                count += 1
            else:
                prev = i
                count = 1
            max_count = max(max_count,count)
        return max_count
            
            
            
                
        