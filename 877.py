class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        l = len(piles)
        dp = [['' for i in range(l)] for j in range(l)]
       
        def find(start, end, turn) :
            if(start == end) :
                if(turn) :
                    dp[start][end] = piles[start]
                else :
                    dp[start][end] = -piles[end]
                return dp[start][end]
            if(dp[start][end] != '') :
                return dp[start][end]
            if(turn ) :
                dp[start][end] = max(piles[start] + find(start + 1, end, False), 
                                      piles[end] + find(start, end - 1, False))
            else :
                dp[start][end] = max( find(start + 1, end, False) - piles[start], 
                                      find(start, end - 1, False) - piles[end])
            
            return dp[start][end]
    
        find(0, l - 1, True)
        return dp[0][l-1]
        