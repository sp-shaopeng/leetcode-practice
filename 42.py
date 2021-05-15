class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
#         maxl = []
#         maxr = []
#         toAdd = 0
#         c = 0
#         for i in range(len(height)) :
#             c = max(c, height[i])
#             maxl.append(c)
            
#         c = 0
#         for i in range(len(height) - 1, -1, -1) :
#             c = max(c, height[i])
#             maxr.insert(0,c)
        
#         for i in range(len(height)):
#             v = min(maxl[i], maxr[i]) - height[i]
#             if(v > 0) :
#                 toAdd += v
#         return toAdd

# Double pointer
            
        toAdd = 0
        h = len(height)
        if(h == 0) :
            return toAdd
        L = 0
        R = h - 1
        ML = height[0]
        MR = height[R]
        while(L < R):
            if(ML <= MR):
                L = L + 1
                v = height[L]
                if(ML > v) :
                    toAdd += ML - v
                else:
                    ML = v
            else:
                R = R - 1
                v = height[R]
                if(MR > v) :
                    toAdd += MR - v
                else:
                    MR = v
        return toAdd
        
        
        
        
        
        