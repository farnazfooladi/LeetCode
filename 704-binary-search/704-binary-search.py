class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        
        
        while l <= r:
            piv = l + (r-l)//2
            if target == nums[piv]:
                return piv
            if target < nums[piv]:
                r = piv - 1
            else:
                l = piv + 1
                
        return -1
    
    
    
        #     low, high = 0, len(nums) - 1
        # while low <= high:
        #     mid = low + (high-low)//2
        #     if target == nums[mid]:
        #         return mid
        #     if target < nums[mid]:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return -1
            
                
            
        