class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_list = []
        for x, y in points:
            distance = ((x**2)+(y**2))
            heap_list.append([distance, x, y])
            
        heapq.heapify(heap_list)
        print(heap_list)
        result = []
        while k > 0:
            d, x, y = heapq.heappop(heap_list)
            result.append([x, y])
            k -= 1
        print(result)
        return result
        