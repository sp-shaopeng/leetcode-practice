        if(l == 1):
            return nums[0]
        
        d = {}
        
        for i in nums:
            d[i] = d.get(i,0) + i
        
        k = d.keys()
        k.sort()
        print(d)
        
        c = 0
        pp = k[0]
        p = k[1]
        
        if(p >  pp + 1) :
            d[p] = d[p] + d[pp]
        
        for i in range(2,len(k)) :
            v = k[i]
      
            if(v > p+1) :
                d[v] = max(d[v] + d[p], d[v] + d[pp])
                
            else :
                d[v] = max(d[v] + d[pp], d[v] + c)
            
            c = max(c, d[pp])
            pp = p
            p = v  
        
        return max(d[pp],d[p])
            