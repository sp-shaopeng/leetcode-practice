class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dp = [999999 for i in range(l)]
        dp[-1] = 0
        
        for i in range(l-2, -1, -1):
            move = 9999999   
            for j in range(1, nums[i] + 1):
                if(i + j > l - 1):
                    break
                move = min(move, 1 + dp[i + j])
            
            dp[i] = move
        return dp[0]
            
        
        