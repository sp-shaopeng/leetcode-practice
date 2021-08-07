class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        
        
        
        l = len(arr)
        ar = [arr[0]]
        for i in range(1, l) :
            if(arr[i] != arr[i - 1]) :
                ar.append(arr[i])
        arr = ar
        l = len(arr)        
        d = set()
        
        def find(pos, v) :
            if(pos < l) :
                v |= arr[pos] 
                if(v not in d) :
                    d.add(v)
                find(pos + 1, v)
                find(pos + 1, 0)
        

        find(0, 0)
        return len(d)