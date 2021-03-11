class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        def find(res, remain) :
            if(len(remain) == 0 and res not in ans):
                ans.append(res)
            
            for i in range(len(remain)):
                a = res[:]
                a.append(remain[i])
                res1 = remain[0:i] + remain[i+1:]
                find(a, res1)
        find([], nums)
        return ans