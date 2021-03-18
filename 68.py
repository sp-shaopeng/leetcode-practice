class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        l = [len(i) for i in words]
        ans = []
        s = []
        sl = 0
        for j in range(len(words)) :
            if(sl + l[j] > maxWidth):
                ans.append(s)
                sl = l[j] + 1
                s = []
                s.append(words[j])
            else:
                sl = sl + l[j] + 1 
                s.append(words[j])
                
                if(sl >= maxWidth) :
                    ans.append(s)
                    sl = 0
                    s = []
        if(sl > 0) :
            ans.append(s)
        for i in range(len(ans)):
            if(i != len(ans) - 1) :
                j = len(ans[i])
                out = " ".join(ans[i])
                lout = len(out)
                if(lout < maxWidth):
                    d = maxWidth - lout
                    if(j > 1):
                        numS = j - 1
                        f = d / numS
                        f = f + 1
                        r = d % numS
                        # print(i,f,r)
                        out = out.replace(" ", " "*f)
                        out = out.replace(" "*f, " "*(f+1), r)
                    else:
                        out += " " * d
            else:
                out = " ".join(ans[i])
                lout = len(out)
                d = maxWidth - lout
                out += " " * d
            o.append(out)
        return o
            
            
            
            
            
                
                