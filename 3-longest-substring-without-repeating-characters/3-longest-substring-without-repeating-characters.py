class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a_list = []
        maxLen = 0
        for i in s:
            if i in a_list:
                a_list = a_list[a_list.index(i)+1:]
                
            a_list.append(i)
            maxLen = max(maxLen, len(a_list))
        return maxLen
    


            
            
        