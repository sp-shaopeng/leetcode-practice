class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums) - 1
        while(l > 0 and nums[l - 1] >= nums[l]):
            l -= 1
        
        if(l == 0) :
            nums[:] = nums[::-1]
            return 
        
        j = len(nums) - 1
        while( j >= 0 and nums[j] <= nums[l - 1]):
            j -= 1
        
        nums[j], nums[l - 1] = nums[l - 1], nums[j]
        
        nums[l: ] = nums[len(nums) - 1 : l - 1 : -1]
        