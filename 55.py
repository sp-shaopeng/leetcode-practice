class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        
        m = 0
        for i in range(l):
            if(m < i) :
                return False
            cm = i + nums[i]
            m = max(m, cm)
            if(m >= l - 1):
                return True
            
            
            

            