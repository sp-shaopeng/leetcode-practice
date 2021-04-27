class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 0) :
            return n
        if( n < 3) :
            return 1
        
        ptr = 0
        ptr1 = 1
        ptr2 = 1
        
        for i in range(3, n + 1) :
            v = ptr + ptr1 + ptr2
            ptr = ptr1
            ptr1 = ptr2
            ptr2 = v
        
        return ptr2
        
        