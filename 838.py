class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        
        l = len(dominoes)
        s = dominoes

        ss = s
        for j in range(l) :
            for i in range(l) :
                # print(ss)
                if(s[i] == ".") :
                    R = False
                    L = False
                    if(i > 0 and s[i - 1] == "R") :
                        R = True
                    if(i < l - 1 and s[i + 1] == "L") :
                        L = True
                    # print(i, L, R)
                    if(L and R) :
                        continue
                        
                    if(L):
                        ss = ss[0:i] + 'L' + ss[i+1:]

                    if(R):
                        ss = ss[0:i] + 'R' + ss[i+1:]

                    # print(ss)
            if(ss == s) :
                return ss
            s = ss
        return s