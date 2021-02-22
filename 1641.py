class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1 for i in range(5)]
        
        if(n == 1):
            return 5
        
        for i in range(2, n + 1) :
            for j in range(5):
                r = 0
                for k in range(j, 5):
                    r = r + res[k]
                res[j] = r
        
        ans = 0
        print(res)
        for i in range(5):
            ans = ans + res[i]
        
        return ans
        
        