class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        
        if(N > K + W or K == 0) :
            return 1.0
        
        dp = [0.0] * (N+1)
        dp[0] = 1.0
        s = 1.0
        for i in range(1,N+1):
            p = s / W
            dp[i] = p
            if (i < K) :
                s += p
            
            if( i - W >= 0) :
                s -= dp[i - W]
                
        # dp[0] = 0
        print(dp)
        return sum(dp[K:])
