class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = path.split("/")
        ans = []
        for i in range(len(s)):
            if(s[i] == "..") :
                if(len(ans) > 0) :
                    del ans[-1]
            
            elif(s[i] != '' and s[i] != ".") :
                ans.append(s[i])
        
        m = "/"
        m += "/".join(ans)
        return m