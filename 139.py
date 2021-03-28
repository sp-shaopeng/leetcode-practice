class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        l = len(s)
        dp = [ [-1 for i in range(l + 1)] for j in range(l + 1)]

        def find(start, end) :
            if(dp[start][end] != -1) :
                return dp[start][end]

            if(end <= start) :
                return 0

            if(s[start:end] in wordDict) :
                dp[start][end] = 1
                return 1

            for i in range(start + 1, end) :
                dp[start][end] = find(start, i) and find(i, end)
                if(dp[start][end] == 1) :
                    dp[start][end] = 1
                    return 1
            dp[start][end] = 0
            return 0

        find(0, l)
        return dp[0][l]

