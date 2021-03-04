class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 0):
            return 1
        ans = 1
        product = 9
        for i in range(0,n -1) :
            ans += product
            product = product * (9 - i)
        return ans + product
        
        
        