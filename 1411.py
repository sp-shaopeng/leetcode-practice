class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        threeColor = 6
        twoColor = 6
        
#       if i have 3 color: rgb, next can be gbg, gbr, grg, brg
#       if i have 2 color: rgr, next can be grg, gbg, brb, grb, brg
#       so each 3 color leads to 2 2color and 2 3color
#       each 2 color leads to 2 3color and 3 2color
        
        
        for i in range(1,n):
            a = threeColor * 2 + twoColor * 2
            b = threeColor * 2 + twoColor * 3
            threeColor = a
            twoColor = b
        
        return (threeColor + twoColor) % (10 ** 9 + 7)