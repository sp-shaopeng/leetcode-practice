# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        i = 0
        low = 0
        high = 1
        while(reader.get(high) != 2 ** 31 - 1) :
            high = 2 * high
            
        while(low < high) :
            mid = (low + high) / 2
            if(reader.get(mid) == target) :
                return mid
            if(reader.get(mid) < target) :
                low = mid + 1
            else :
                high = mid - 1
        
        if(reader.get(low) == target) :
            return low
        return -1