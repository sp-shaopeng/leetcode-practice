class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums) 
        mem = [-1] * l
        mem[0] = 1
        
        def dp(nums, pos):
            if(mem[pos] == -1):
                p = nums[pos]
                m = 1;
                mem[pos] = 1
                for i in range(pos):
                    if(mem[i] == -1) :
                        dp(nums, i);
                    if(p > nums[i]) :
                        if(mem[i] + 1 > m):
                            m = mem[i] + 1
                            mem[pos] = m
                        
        dp(nums, l - 1);
        
        print(l)
        print(mem)
        ans = 0
        for i in range(l):
            if (ans < mem[i]):
                ans = mem[i]
        
        
                       
        return ans