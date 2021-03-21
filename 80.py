class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = 1
        tail = 1
        l = len(nums)
        count = 1
        curr = nums[0]
        while(tail < l and head < l):
            if(nums[tail] != curr) :
                nums[head] = nums[tail]
                count = 1
                curr = nums[head]
                head += 1
                tail += 1
                continue
            if(nums[tail] == curr and count < 2):
                nums[head] = nums[tail]
                count += 1    
                head += 1
                tail += 1
                continue
            else:
                tail += 1
        
        return head
                
                
                