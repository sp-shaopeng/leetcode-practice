class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        d = {}
        for i in magazine :
            d[i] = d.get(i, 0) + 1
        
        for j in ransomNote :
            v = d.get(j, 0)
            if(v == 0) :
                return False
            else :
                d[j] = d.get(j) - 1
        return True
        