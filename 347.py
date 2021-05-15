class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        ntf = {}
        ftn = {}
        
        for i in range(len(nums)) :
            v = nums[i]
            
            if(v in ntf) :
                f = ntf[v]
                ntf[v] = f + 1
                ftn[f].remove(v)
                
                if((f+1) in ftn) :
                    ftn[f + 1].add(v)
                else :
                    ftn[f + 1] = {v}
                    
            else :
                ntf[v] = 1
                if(1 in ftn) :
                    ftn[1].add(v)
                else :
                    ftn[1] = {v}
        
        
        f = ftn.keys()
        f.sort()
        
        ans = []
        ptr = len(f) - 1
        
        while(k > 0 and ptr >= 0):
            s = list(ftn[f[ptr]])
            
            ans += s
            ptr = ptr - 1
            k = k - len(s)
        
        return ans
        
        
        
        