# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        
        right = mountain_arr.length() - 1
        left = 0
        while(left < right) :
            mid = (left + right) / 2
            if(mountain_arr.get(mid ) < mountain_arr.get(mid + 1)) :
                left = mid + 1
            else:
                right = mid 
        peak = right
        
        left = 0
        while(left <= peak) :
            mid = (left + peak) / 2
            if(mountain_arr.get(mid) == target) :
                return mid
            if(mountain_arr.get(mid) < target) :
                left = mid + 1
            else:
                peak = mid - 1
            
        peak = right
        right = mountain_arr.length() - 1
        
        while( peak <= right) :
            mid = (right + peak) / 2
            if(mountain_arr.get(mid) == target) :
                return mid
            if(mountain_arr.get(mid) > target) :
                peak = mid + 1
            else:
                right = mid - 1
                
        return -1