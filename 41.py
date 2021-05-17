class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        for i in range(l):
            if(nums[i] <= 0) :
                nums[i] = l + 1

        for i in range(l) :
            v = abs(nums[i])
            
            if(v <= l and v > 0) :
                v = v - 1
                if(nums[v] >= 0) :
                    nums[v] = nums[v] * -1
        for i in range(l) :
            if(nums[i] > 0) :
                return i + 1
        return l + 1