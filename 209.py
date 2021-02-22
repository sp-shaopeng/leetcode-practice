class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min1 = 99999
        l = len(nums)
        head = 0
        tail = 0
        counter = 0
        for tail in range(l):
            counter += nums[tail]       
         
                
            while(counter >= target) :
                d = tail - head + 1
                print("ht",head, tail)
                print(d,min1)
                min1 = min(min1, d)
                counter = counter - nums[head]
                head = head + 1
                
        if(min1 == 99999) :
            return 0
        return min1