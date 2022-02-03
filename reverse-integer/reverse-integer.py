class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN = -2147483648
        MAX = 2147483647
       
        res = 0
        flag = False
        if(x < 0):
            flag = True
        while x:
            digit = int(math.fmod(x, 10))
            x = int(abs(x)//10)
            if (flag==True):
                x = x*-1
            
            print(x)
            print(digit)
            
            # if(res > MAX/10 or (res == MAX/10 and digit > 7)):
            #     return 0
            # if(res < MIN/10 or (res == MIN/10 and digit < -8)):
            #     return 0
            
            if(res > MAX//10 or (res == MAX//10 and digit > MAX%10)):
                return 0
            if(res < MIN//10 or (res == MIN//10 and digit < MIN%10)):
                return 0
            res = (res*10) + digit
            print(res)
            print("------")
        return res