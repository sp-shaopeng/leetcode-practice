class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        newl = n
        e = []
        if(n == 1):
            return True
        while(newl != 1):
            if(newl in e):
                break
            e.append(newl)
  
            t = newl
            newl = 0
            while(t > 0):
                v = t%10
                newl += v * v
                t = t/10
            if(newl == 1):
                return True
        
        return False