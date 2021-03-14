class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        l = len(nums)
        s = sum(nums)
        if(s % 2 == 1):
            return False
        nums.sort()
        dp = [[-1 for i in range(s/2 + 1)] for j in range(l)]
        # for i in range(l) :
        #     dp[i][nums[i]] = True
        
        
        def find(val, pos):
            if(dp[pos][val] != -1) :
                return dp[pos][val]
            
            if(val - nums[pos] < 0) :
                dp[pos][val] = False
            
            if(val - nums[pos] == 0) :
                dp[pos][val] = True
                return True
            
            if(pos > 0):
                dp[pos][val] = find(val - nums[pos], pos - 1) or find(val, pos - 1)
            else:
                dp[pos][val] = False
            return dp[pos][val]
        
        find(s/2, l - 1)
        return dp[l - 1][s/2]
        
        
        
        
        