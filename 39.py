class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        
        def find(pos, val, ls):
            
            if(val == target) :
                if(ls not in ans) :
                    ans.append(ls)
                    
            if(pos == len(candidates) or val > target) :
                return
            
            p = candidates[pos]
            a = ls[:]
            a.append(p)
            find(pos, val + p, a)
            find(pos + 1, val, ls)
    
            
        
        find(0, 0, [])
        return ans
                
                