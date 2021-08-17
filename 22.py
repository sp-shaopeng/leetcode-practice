class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        d = {}
        
        
        def gen(v) :
            if(v in d) :
                return d[v]
            if(v == 1) :
                d[1] = ["()"]
                return d[1]
            else :
                s = gen(v - 1)
                newS = []
                for p in s :
                    newS.append("(" + p + ")")
                    newS.append("()" + p)                    
                    newS.append(p + "()")    
                
                for i in range(2, v/2 + 1) :
                    a = gen(i)
                    b = gen(v - i)
                    for m in a :
                        for n in b:
                            newS.append(m + n)
                            newS.append(n + m)
                
                
                s = list(dict.fromkeys(newS))
                s.sort()
                d[v] = s
            return s
        
        return gen(n)