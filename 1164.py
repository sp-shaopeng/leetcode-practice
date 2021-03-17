class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        even = sum(nums[0::2])
        odd = sum(nums[1::2])
        l = len(nums)
        ans = 0
        ce = 0
        co = 0
        for i in range(l) :
            if(i % 2 == 0) :
                checkE = ce + odd - co 
                checkO = co + even - ce - nums[i]
                if(checkE == checkO) :
                    print(i, "E")
                    ans = ans + 1
                ce = ce + nums[i]
            else :
                checkE = ce + odd - co - nums[i]
                checkO = co + even - ce 
                if(checkE == checkO) :
                    ans = ans + 1
                co = co + nums[i]
        return ans
                