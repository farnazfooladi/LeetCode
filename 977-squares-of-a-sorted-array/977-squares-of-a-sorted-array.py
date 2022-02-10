class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[left] * nums[left] < nums[right] * nums[right]:
                result.append(nums[right] * nums[right])
                right -= 1
            else:
                result.append(nums[left] * nums[left])
                left += 1
        return result[::-1]
            
        