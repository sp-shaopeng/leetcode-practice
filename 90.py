class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        
        def find(n, ls) :
            if(n == -1) :
                ls.sort()
                if(ls not in ans):
                    ans.append(ls)
            else :
                a= ls[:]
                ls.append(nums[n])
                find(n - 1, ls)
                find(n - 1, a)
        find(len(nums) - 1, [])
        return ans