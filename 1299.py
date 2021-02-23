class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l = len(arr) - 1
        largest = arr[l]
        arr[l] = -1
        l = l - 1

        while(l >= 0):
            v = arr[l]
            arr[l] = largest
            if(largest < v):
                largest = v
            l -= 1
                
        return arr
        