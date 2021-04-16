class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        
        s = len(heights)
        m = 0
        stack = []
        left = -1
        i = 0
        while( i <= s) :
            if(i == s) :
                v = 0
            else :
                v = heights[i]
            if(len(stack) == 0 or v >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            else :
                curr = stack.pop()                
                r = i - 1
                
                if(len(stack) == 0) :
                    l = 0
                else:
                    l = stack[-1] + 1
                
                width = r - l + 1
                
                m = max(m, width * heights[curr])
        return m                
        
        
        