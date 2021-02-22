class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        print(s)
        
        g = ["" for i in range(numRows)]
        r = numRows * 2 - 2
        if(r == 0):
            return s
        
        l = len(s)
        
        for i in range(0, l):
            
            v = i % r
            if ( v < numRows) :
                g[v] = g[v] + s[i]
            else:
                p = v % numRows
                p = numRows - 2 - p
                g[p] = g[p] + s[i]
            
                
        ans = ""
        for i in range(numRows):
            ans = ans + g[i]
            
        return ans