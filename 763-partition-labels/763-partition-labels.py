class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        last_inx = {}
        
        for i, c in enumerate(s):
            last_inx[c] = i
            
        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            if last_inx[c] > end:
                end = last_inx[c]
            if i == end:
                res.append(size)
                size = 0
        return res
            
        