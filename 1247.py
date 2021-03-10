class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
        a = len(s1)
        b = len(s2)
        if(a != b):
            return -1
        
        aa = []
        bb = []
        for i in range(a):
            if(s1[i] != s2[i]):
                aa.append(s1[i])
                bb.append(s2[i])
                
        ax = aa.count("x")
        ay = aa.count("y")
        
        bx = bb.count("x")
        by = bb.count("y")
        
        if((ax + ay) % 2 == 1):
            return -1
        
        ans = 0
        axe = ax / 2
        aye = ay / 2
        ans += axe + aye + (ax - 2 * axe) + (ay - 2 * aye)
        return ans
        
        
        
        
        