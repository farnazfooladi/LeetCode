class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
#         charSet = set()
#         l = 0
#         res = 0
        
#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[l])
#             res = max(res, r-l+1)
#         return res
        
        
        
        
        
        
        
        a_list = []
        maxLen = 0
        for i in s:
            if i in a_list:
                a_list = a_list[a_list.index(i)+1:]
                
            a_list.append(i)
            maxLen = max(maxLen, len(a_list))
        return maxLen
    


            
            
        