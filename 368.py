class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        if(l == 0) :
            return []
        dp = [0 for i in range(l)]
        nums.sort()
        dp[0] = [nums[0]]
        for i in range(1,l):
            sets = []
            for j in range(i):
                if(nums[i] % nums[j] == 0 and len(dp[j]) > len(sets)):
                    sets = dp[j][:]
            sets.append(nums[i])
            dp[i] = sets
        
        m = []
        l = -1
        for i in dp:
            if(len(i) > l):
                l = len(i)
                m = i
        return m
        
        
        
        