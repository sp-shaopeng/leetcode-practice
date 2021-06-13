class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = nums[0]
        
        for i in range(1, len(nums)) :
            nums[i] += nums[i - 1]
            m = min(nums[i], m)
        
        if(m > 0) :
            return 1
        else:
            return 1 - m