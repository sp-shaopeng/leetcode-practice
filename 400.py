import math
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = 1
        v = n
        t = v/1.0
        num = 1
        while(True):
            t = v
            v -= d * 9 * num
            if(v <= 0) :
                break
            d = d * 10
            num += 1
        num = num * 1.0
        pos = int(math.ceil(t/num))
        digit = t % int(num)
        val = d + pos - 1
        p = int(digit - 1)
        return str(val)[p]
        
        
        
        
        