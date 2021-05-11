class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        sArr = list(s)
        dp = [[-1 for i in range(n)] for j in range(n)]
        ans = [0]
        def count(l, r) :
            if(sArr[l] == sArr[r] and dp[l][r] == -1 and l <= r) :
                ans[0] += 1
                dp[l][r] = 1
                if(l > 0 and r < n - 1) :
                    count(l - 1, r + 1)
                if(l > 0 and (dp[l][r-1] == 1 or l > r - 1) ) :
                    count(l - 1, r)
                if(r < n - 1 and (dp[l + 1][r] == 1 or l > r - 1)) :
                    count(l, r + 1)
                
        for i in range(n):
            count(i,i)
             
        return ans[0]
                    
        