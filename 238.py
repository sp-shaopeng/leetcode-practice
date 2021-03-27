class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        allZero = False
        noZero = 1;
        oneZero = False
        
        l = len(nums)
        
        for i in nums :
            if(i == 0) :
                if(oneZero):
                    allZero = True
                    break
                else:
                    oneZero = True
            else:
                noZero *= i
        if(allZero) :
            return [0] * l
        else:
            ans = [0 for i in range(l)]
            
            for i in range(l):
                if(oneZero and nums[i] == 0) :
                    ans[i] = noZero
                elif(oneZero) :
                    ans[i] = 0
                else:
                    ans[i] = noZero / nums[i]
            return ans