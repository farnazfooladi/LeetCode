class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        HashMap = {}
        
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                HashMap[stack.pop()] = nums2[i]
            stack.append(nums2[i])
            
        while stack:
            HashMap[stack.pop()]=-1
            
        
        res = [0] * len(nums1)
        for i in range(len(nums1)):
            res[i] = HashMap[nums1[i]]
            
        return res
        