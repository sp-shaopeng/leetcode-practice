class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        
        
        isNegative = False
        
        if (x < 0):
            x = -x
            isNegative = True
        
        
        
        while(x > 0) :
            d = x % 10
            ans = ans * 10 + d
            x = x / 10;
        
        if(isNegative) :
            ans = -ans
        
        if(ans > (2 ** 31 - 1) or ans < (-2**31 -1)):
        
            return 0
        
        return ans