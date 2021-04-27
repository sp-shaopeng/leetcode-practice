class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if(n <= 2) :
            return n
        
        ptr, ptr1 = 1, 2
        
        for i in range(3, n + 1) :
            v = ptr1 + ptr
            ptr = ptr1
            ptr1 = v
        
        return ptr1
        