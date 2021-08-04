class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        dp = [0 for i in range(l)]
        count = [0 for i in range(l)]
        
        
        def find(pos) :
            dp[pos] = 1 + findMax(nums[pos], pos)
        
        def findMax(num, pos) :
            res = 0
            c = 1
            
            for i in range(pos + 1, l) :
                if(num < nums[i]) :
                    if(dp[i] > res) :
                        res = dp[i]
                        c = count[i]
                    elif(dp[i] == res) :
                        c += count[i]
          
            count[pos] = c
                
            return res
        
        for i in range(l - 1, -1, -1):
            find(i)
        m = max(dp)
        r = 0
        for i in range(l) :
            if(dp[i] == m) :
                r += count[i]
        return r
                    

