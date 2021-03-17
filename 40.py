class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        
        def find(pos, val, ls):
            
            if(val == target) :
                ls.sort()
                if(ls not in ans) :
                    ans.append(ls)
                    
            if(pos == len(candidates) or val > target) :
                return
            
            p = candidates[pos]
            a = ls[:]
            a.append(p)
            find(pos + 1, val + p, a)
            
            newPos = pos + 1
            while(True) :
                if(newPos == len(candidates)) :
                    return
                      
                if(candidates[pos] != candidates[newPos]):
                    find(newPos, val, ls)
                    return
                
                newPos += 1

        
        find(0, 0, [])
        return ans