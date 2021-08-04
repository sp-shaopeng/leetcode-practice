class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        
        l = len(target)
        ptr = 0
        res = []
        for i in range(1, n+1) :
            if(ptr == l) :
                break
            if(target[ptr] != i) :
                res.append("Push")
                res.append("Pop")
            else :
                res.append("Push")                
                ptr += 1
        return res