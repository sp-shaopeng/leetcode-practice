class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = nums[0]
        l = len(nums)
        ans = m
        for i in range(1,l) :
            c = m + nums[i]
            ans = max(ans, m)      
            if(c < nums[i]) :
                m = nums[i]
            else:
                m = c
        return max(ans,m)