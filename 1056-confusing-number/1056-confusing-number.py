class Solution:
    def confusingNumber(self, n: int) -> bool:
        if n == 0 : return False 
        dum = n 
        D = {
            0:0,
            1:1,
            6:9,
            8:8,
            9:6,
        }
        st = set(D.keys())
        _str = "" 
        while n: 
            n, mod = divmod(n,10)
            if mod not in st:
                return False 
            print(_str)
            _str += str(D[mod]) 
        if int(_str) == dum: return False 
        return True 
        