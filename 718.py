class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        l1 = len(nums1)
        l2 = len(nums2)
        dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
        
        c = 0
        
        for i in range(1, l1 + 1) :
            for j in range(1, l2 + 1) :
                if(nums1[i - 1] == nums2[j - 1]) :
                    dp[i][j] = dp[i-1][j-1] + 1    
                    c = max(c, dp[i][j])
        return c
         