class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxheap =[]
        count = Counter(s) # Hashmap, count each char
        maxheap = [[-cnt, char] for char, cnt in count.items()]

        # for char, cnt in count.items():
        #     heapq.heappush(maxheap, (-cnt, char))
        heapq.heapify(maxheap) # O(n)
        
        print(maxheap)
        
        prev = None
        res = ""
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            # most frequent, except prev
            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt += 1
            
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res
        