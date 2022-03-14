class StockSpanner(object):

    def __init__(self):
        self.stack = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if len(self.stack) == 0:
            self.stack.append((price,1))
            return 1
        sp = 0
        
        while len(self.stack) != 0 and self.stack[-1][0] <= price:
            p, s = self.stack.pop()
            sp += s
        
        span = sp + 1
        
        self.stack.append((price, span))
        
        return span
            
            
            
            
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)