class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        
        horizontalCuts.append(0)
        horizontalCuts.append(h)

        verticalCuts.append(0)
        verticalCuts.append(w)
        
        horizontalCuts.sort()
        verticalCuts.sort()
        maxH = 0
        maxW = 0
        for i in range(1, len(horizontalCuts)):
            v = horizontalCuts[i] - horizontalCuts[i - 1]
            maxH = max(v, maxH)
        
        for i in range(1, len(verticalCuts)):
            v = verticalCuts[i] - verticalCuts[i - 1]
            maxW = max(v, maxW)  
        
        print(maxW, maxH)
        return (maxW * maxH) % (1000000000 + 7)
        
        
        
        
        
        
        