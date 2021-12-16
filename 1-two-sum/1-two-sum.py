class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return false
        
        a_dict = {}
        total = 0
        for i in range(len(nums)):
            total = target - nums[i]
            if total in a_dict:
                return [a_dict[total],i]
            else:
                a_dict[nums[i]] = i
            
                
            
            
            
        