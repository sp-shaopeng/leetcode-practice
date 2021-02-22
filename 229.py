class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        threshold = l/3
        
        a = {}
        for num in nums:
            if num in a:
                a[num] += 1
            else:
                a[num] = 1
        ans = []
        for key in a:
            if(a[key] > threshold):
                ans.append(key)
                
        return ans