class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        l = len(nums)
        
        appear = [{} for i in range(l)]
        
        if(nums[0] != 0):
            appear[0] = {nums[0]:1, -nums[0]: 1}
        else:
            appear[0] = {0:2}
       
        def find(pos, val):
            if(-val in appear[pos]):
                return appear[pos].get(-val)
            
            if(pos == 0):
                return 0
            
            a = find(pos - 1, val + nums[pos])
            b = find(pos - 1, val - nums[pos])
            
            appear[pos][val] = a + b
            return a + b
        
#         Top down recurssion is too slow
#         find(l - 1, S)




        for i in range(1,l):
            ls = {}
            # print(i)
            for k in appear[i-1]:
                ls[k + nums[i]] = ls.get(k+nums[i],0) + appear[i-1].get(k)
                ls[k - nums[i]] = ls.get(k-nums[i],0) + appear[i-1].get(k)
            appear[i] = ls
        return appear[-1].get(S,0)
    
                
            
            
            