class MedianFinder:

    def __init__(self):
        # Two heaps: large -> minHeap, small -> maxHeap
        # Heaps should be the same size or difference be only 1
        self.small = []
        self.large = []
        
    def addNum(self, num: int) -> None:
        # By default we add the numbers to the small heap then we check for the size
        heapq.heappush(self.small, -1 * num)
        
        # if the small > large then pop small and push large
        if(self.small and self.large and (-1 * self.small[0] > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # un even size of each heap
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0])/2
        
            
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()