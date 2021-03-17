class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        ans = []
        def find(pos, val, ls, k):
            
            if(k == 0 and val == 0) :
                ls.sort()
                if(ls not in ans) :
                    ans.append(ls)
                return 
                    
            if(pos == 10 or val < 0) :
                return
            
            a = ls[:]
            a.append(pos)
            find(pos + 1, val - pos, a, k - 1)
            
            find(pos + 1, val, ls, k)

        
        find(1, n, [], k)
        return ans