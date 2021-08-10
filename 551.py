class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        a = [i for i in s]
        if(a.count("A") >= 2) :
            return False
        else :
            c = 0
            for i in range(len(a)) :
                if(i == 0 and a[0] == "L") :
                    c = 1
                elif(a[i] == 'L' and a[i-1] == 'L') :
                    c += 1
                elif(a[i] == 'L') :
                    c = 1
                if(c >= 3) :
                    return False
            return True
        
        