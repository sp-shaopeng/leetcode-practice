class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        l = len(nums)
        
        pivot = nums[0]
        
        if(l == 1):
            return pivot == target
        
        if(target == pivot) :
            return True
        
        if(target > pivot) :
            c = 1
            while (c < l):
                if(nums[c] == target):
                    return True
                if(nums[c] > target):
                    print("b")
                    
                    break;
                
                c += 1
        else:
            c = l - 1
            while( c >= 0):
                print(nums[c])
                if(nums[c] == target):
                    return True
                if(nums[c] < target):
                    print("b")
                    break;
                c -= 1
                
        return False