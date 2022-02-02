class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for a in asteroids:
            #Collision condition 
            #(stack not empty and left element negative and right element positive)
            while stack and a < 0 and stack[-1] > 0:
                diff = a + (stack[-1])
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    #destroy a
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
                
        