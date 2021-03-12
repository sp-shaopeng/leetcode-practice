class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        
        ans = []
        
        def find(n, s) :
            while( n < len(S) and (not str(s[n]).isalpha()) ):
                n += 1
                
            if(n == len(S)):
                ans.append(s)
                return
            
            a = s
            b = s
            a = a[0:n] + a[n].upper() + a[n + 1:]
            find(n + 1,str(a))
            find(n + 1,str(b))
    
        find(0, S.lower())
        return ans