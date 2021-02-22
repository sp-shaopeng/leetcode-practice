class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def pow(a, p):
            if(p == 0):
                return 1
            
            if(p % 2 == 1):
                return a * pow(a, p-1)
            else:
                v = pow(a, p/2)
                return v*v
        
        if(n < 0) :
            n = -n
            return 1/pow(x,n)
        else:
            return pow(x,n)