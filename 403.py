class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        
        dic = collections.defaultdict(set)
        dic[0].add(0)
        for i in range(len(stones)):
            if(stones[i] in dic):
                for v in dic[stones[i]]:
                    
                    if(v > 1) :
                        dic[stones[i] + v - 1].add(v - 1)
                    dic[stones[i] + v].add(v)
                    dic[stones[i] + v + 1].add(v + 1)
                    
        if(stones[-1] in dic):
            return True
                
        return False
        