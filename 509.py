class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n <= 1) :
            return n 
        
        ptr = 0
        ptr1 = 1
        
        for i in range(2, n + 1) :
            v = ptr + ptr1
            ptr = ptr1
            ptr1 = v
        
        return ptr1