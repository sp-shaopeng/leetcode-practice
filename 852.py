class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if(len(arr) == 1) :
            return 0
        
        for i in range(len(arr)) :
            if(i < len(arr) - 1 and arr[i] > arr[i+1]) :
                return i
            
            if(i == len(arr) - 1) :
                return i