class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        dp = [1] * n
        v2 = 1
        v3 = 1
        v5 = 1
        p2 = p3 = p5 = -1
        m = 0
        for j in range(n):
            m = min(v2,v3,v5)
            dp[j] = m
            dp[j] = m
            if(m == v2) :
                p2 += 1
                v2 = dp[p2] * 2
            
            if(m == v3) :
                p3 += 1
                
                v3 = dp[p3] * 3
                
            if(m == v5) :
                p5 += 1
                
                v5= dp[p5] * 5
        return m
     
            