class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if(l < 2):
            return 0
        
        nums.sort()
        
        m = 0
        for i in range(l - 1):
            if(m < nums[i+1] - nums[i]):
                m = nums[i+1] - nums[i]
                
        return m