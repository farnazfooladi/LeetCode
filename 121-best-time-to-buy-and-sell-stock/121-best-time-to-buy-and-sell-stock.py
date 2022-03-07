class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_prof = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_prof:
                max_prof = prices[i] - min_price
        
        return max_prof
    
    
    
    
    
    
    
    
#         new_list = {}
#         for i, price in enumerate(prices):
#             new_list[price] = i
#         print(new_list)
        
        
#         heapq.heapify(prices)
#         # print(prices)
#         cheapest = heapq.heappop(prices)
#         cheapestDay = new_list[cheapest]
        
#         # dic_key = list(new_list.keys())
#         # print(dic_key)
#         # cheapestDay = dic_key.index(cheapest)
#         # print(cheapestDay)
#         max_val = 0
        
#         for i in range(cheapest, len(prices)):
#             result = 0
#             if  > cheapestDay:
#                 result =  new_list[i] - cheapest
#                 print(result)
#                 max_val = max(max_val, result)
#         return max_val
            
            
            
            
        