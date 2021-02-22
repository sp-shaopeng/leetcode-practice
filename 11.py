class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#         ans = -1;
#         total = len(height)
#         for i in range (total) :
#             v = height[i]
#             for j in range(i + 1, total) :
#                 w = height[j]
#                 area = v * (j - i)
#                 if(w < v) :
#                     area = w * (j - i)
#                 if (area > ans) :
#                     ans = area
                    
#         return ans
        ans = -1
        head = 0
        tail = len(height) - 1
        while (head < tail) :
            h = tail - head
            v = height[tail]
            if(height[head] < height[tail]) :
                v = height[head]
            
            area = h * v
            if(area > ans) :
                ans = area
            
            if(height[head] < height[tail]) :
                head += 1
            else :
                tail -= 1
        
        return ans
            
            
            
