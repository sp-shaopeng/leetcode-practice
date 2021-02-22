class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        if(b == 0):
            return a*'a'
        if(a == 0):
            return b*'b'
        
        if(a > b):
            return "aab" + self.strWithout3a3b(a-2, b-1)
        if(b > a):
            return "bba" + self.strWithout3a3b(a-1, b-2)
        if(b == a):
            return "ab" + self.strWithout3a3b(a-1, b-1)
        return ""
        