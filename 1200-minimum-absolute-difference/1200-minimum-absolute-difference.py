class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        result = []
        minPair = float("inf")
        for i in range(len(arr)-1):
            minPair = min(minPair, arr[i+1] - arr[i])
        
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == minPair:
                result.append([arr[i],arr[i+1]])
        return result
            
        