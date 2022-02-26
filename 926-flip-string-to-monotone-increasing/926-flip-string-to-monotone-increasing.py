class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero = s.count("0")
        one = 0
        output = zero
        
        for digit in s:
            if digit == "0":
                zero -= 1
            if digit == "1":
                one += 1
            output = min(output, zero+one)
        return output
            
        