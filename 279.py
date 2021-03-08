class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if(n < 2) :
            return n
        
        s = int(math.sqrt(n))
        if(s*s == n) :
            return 1
        
        dp = [0] * s
        for i in range(s):
            dp[i] = (i + 1) ** 2
        queue = [n]
        d = 0
        while(queue):
            newQ = []
            d += 1
            while(queue) :
                v = queue.pop()
                for p in dp:
                    newV = v - p
                    if(newV == 0):
                        return d 
                    if(newV > 0) :
                        newQ.append(newV)
                    else:
                        break
            queue = newQ
            
        return 0
            

        
            