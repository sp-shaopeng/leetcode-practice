class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(sum(nums))
        
        total = 0
        
        v = [number % 3 for number in nums]
        print(nums)
        
        s = sum(v)
        
        if(s % 3 == 0):
            return sum(nums)
        r = s % 3
        print(s, r)
        
        if(r == 1) :
            p1 = -1
            p2, p22 = -1, -1
            for i in range(len(v)):
                if(p1 == -1 or p2== -1 or p22 == -1):
                    if(p1 == -1 and v[i] == 1):
                        p1 = i
                        if( p22 == -1) :
                            break
                    if(p22 == -1 and v[i] == 2):
                        p22 = p2
                        p2 = i
                else:
                    break
            print(p1,p2,p22)
            if(p22 == -1) :
                return sum(nums) - nums[p1]
            elif(p1 == -1):
                return sum(nums) - nums[p2] - nums[p22]
            else :
                if(nums[p1] > nums[p2] + nums[p22]):
                    return sum(nums) - nums[p2] - nums[p22]
                return sum(nums) - nums[p1]
            
        else:
            p1 = -1
            p2, p22 = -1, -1
            for i in range(len(v)):
                if(p1 == -1 or p2== -1 or p22 == -1):
                    if(p1 == -1 and v[i] == 2):
                        p1 = i
                        
                        if( p22 == -1) :
                            break
                    
                    if(p22 == -1 and v[i] == 1):
                        p22 = p2
                        p2 = i
                else:
                    break
            if(p22 == -1) :
                return sum(nums) - nums[p1]
            elif(p1 == -1):
                return sum(nums) - nums[p2] - nums[p22]
            else :
                if(nums[p1] > nums[p2] + nums[p22]):
                    return sum(nums) - nums[p2] - nums[p22]
                return sum(nums) - nums[p1]
            
        
        
        