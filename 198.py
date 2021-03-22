class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return nums[0]
        
        dp = [-1 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        k = 0
        for i in range(2, len(nums)) :
            dp[i] = max(nums[i] + dp[i - 2], nums[i] + k)
            k = max(k,dp[i - 2])
        return max(dp[len(nums) - 1], dp[len(nums) - 2])
        
        
        
        
        