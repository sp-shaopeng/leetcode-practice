class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans = nums[0]
        neg = nums[0]
        pos = ans
        l = len(nums)
        
        for i in range(1,l):
            v = nums[i]
            ans = max(ans, pos)
            
            if(v == 0) :
                pos = 0
                neg = 0
                continue
            
            if(pos == 0) :
                a = v
            else :
                a = pos * v
            
            if(neg == 0) :
                b = v
            else :
                
                b = neg * v
            
            pos = max(a, b, v)
            neg = min(a, b, v)
        
        return max(ans, pos)
        