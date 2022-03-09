class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = collections.Counter(nums)
        print(x)
        for v in x.values():
            if v > 1:
                return True
            
        return False
        