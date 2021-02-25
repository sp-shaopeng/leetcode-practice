class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        upper = sum(nums)
        lower = 0
        ans = []
        for i in range(l):
            v = nums[i]
            rhs = l - i - 1
            lhs = i
            
            left = lhs * v
            right = rhs * v
            
            upper -= v
            
            leftr = left - lower
            rightr = upper - right
            ans.append(leftr + rightr)
            lower += v
        
        return ans
            