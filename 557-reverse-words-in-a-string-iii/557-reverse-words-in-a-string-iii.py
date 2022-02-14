class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stringReverse = ''
        left = 0
        for i in range(len(s)):
            if s[i] == ' ':
                right = i-1
                while left <= right:
                    stringReverse += s[right]
                    right -= 1
                stringReverse += ' '
                left = i+1
            if i == len(s)-1:
                right = i
                while left <= right:
                    stringReverse += s[right]
                    right -= 1
        return stringReverse
        