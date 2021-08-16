class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        arr = [-1] * 32
        
        for i in nums :
            v = i % 10
            i = i / 10
            p = i % 10
            l = i / 10
            
            pos = 2 ** (l - 1) + p - 2
            arr[pos] = v
        
            
        Q = [[0, 0]]
        s = 0
        while(Q) :
            newQ = []
            while(Q) :
                p, v = Q.pop()
                v += arr[p]
                l = 2 * p + 1
                r = 2 * p + 2
                if(arr[l] == -1 and arr[r] == -1) :
                    s += v
                else :
                    if(arr[l] != -1) :
                        newQ.append([l, v])
                    if(arr[r] != -1) :
                        newQ.append([r, v])
            Q = newQ
        return s
                
            
            
            