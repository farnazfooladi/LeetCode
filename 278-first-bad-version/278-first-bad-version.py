# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low < high:
            mid = low + (high - low) // 2
            if (isBadVersion(mid)):
                high = mid
                
            else:
                low = mid + 1
        return low
                
            
#         vers_num = n
#         result_list = []
        
#         while vers_num > 0:
#             result = isBadVersion(vers_num)
#             if result == True:
#                 result_list.append(vers_num)
#             vers_num -= 1
#         result_list.sort()
#         return (result_list[0])

                
        