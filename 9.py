class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0) :
            return False
        
        y = 0
        c = x
        while(x > 0):
            d = x% 10
            y = y *10 + d
            x = x/10
        while(y>0):
            a = y % 10
            b = c % 10
            if(a != b) :
                return False
            y = y/10
            c = c/10
        return True