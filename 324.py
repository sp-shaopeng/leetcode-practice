class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        l = len(nums)
        mid = 0
        if(l % 2 == 1):
            mid = l/2 
        else:
            mid = l/2 - 1
        
        back = l - 1
        ans = [0] * l
        # print(nums)
        for i in range(l):
            # print(ans)
            print(mid, back)
            if(i%2 == 0):
                ans[i] = nums[mid]
                mid -= 1
            else:
                ans[i] = nums[back]
                back -=1
        for i in range(l):
            nums[i] = ans[i]
        
        # print(nums)
