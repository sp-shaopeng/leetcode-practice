class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        v = "1"
        
        if( n == 1) :
            return v
        
        for i in range(2, n+1) :
            ls = list(v)
            newV = ""
            count = 1
            curr = ls[0]
            for j in range(1, len(ls)) :
                if(ls[j] == curr) :
                    count += 1
                else:
                    newV += str(count) + curr
                    curr = ls[j]
                    j += 1
                    count = 1
            
            newV += str(count) + curr
            v = newV
        
        return v
        
        