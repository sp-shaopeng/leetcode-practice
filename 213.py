class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        
        def find(arr):
            dp = [0 for i in range(l - 1)]
            dp[0] = arr[0]
            dp[1] = arr[1]
            k = 0
            
            for i in range(2, l - 1):
                dp[i] = max(arr[i] + dp[i - 2], arr[i] + k )
                k = max(k, dp[i - 2])
            return max(dp[l-2], dp[l - 3])
        
        if(l == 1) :
            return nums[0]
        elif(l == 2):
            return max(nums)
        else:
            return max(find(nums[1:]), find(nums[:-1]))
            
        
        
        
        