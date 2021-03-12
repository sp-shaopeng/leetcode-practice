class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        
        def find(n, ls):
            if(n == len(nums)):
                
                if(ls not in ans):
                    ans.append(ls)
            else:
                a = ls[:]
                ls.append(nums[n])
                
                find(n + 1, a)
                find(n + 1, ls)
        
        find(0, [])
        return ans
        
        