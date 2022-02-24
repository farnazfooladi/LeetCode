class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        
        box = 0
        unit = 0
        total_unit = 0
        
        boxTypes.sort(key=lambda x: -x[1])
        
        for b, u in boxTypes:
            box = min(truckSize, b)
            total_unit += box*u
            truckSize-=box
            
            if truckSize == 0:
                break
        return total_unit
            
        