class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if(len(stones) == 0):
            return 0
        if(len(stones) == 1):
            return stones[0]
        while(True) :
            a = max(stones)
            stones.remove(a)
            b = max(stones)
            stones.remove(b)
            c = a - b
            if(c != 0):
                stones.append(c)
            if(len(stones) == 0):
                return 0
            
            if(len(stones) == 1):
                return stones[0]
        