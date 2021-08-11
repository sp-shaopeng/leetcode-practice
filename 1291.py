class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        
        res = set()
        
        def sameL(num, k, digit) :
            if(num <= high and k >= 10) :
                if(num >= 123456789) :
                    return 
                v, d, k = findSmallest(digit * 10)
                if(v <= high) :
                    res.add(v)
                    sameL(v, k, d)
                return
            
            v = num % digit
            v *= 10 
            v += k
            if(v >= low and v <= high) :
                res.add(v)
                sameL(v, k + 1, digit)

        
        def findSmallest(num) :
            n = num
            i = 1
            while(num >= 10) :
                num = num / 10
                i += 1
            res = 0
            d = 1
            v = 0
            for j in range(i):
                if(num >= 10) :
                    break
                d *= 10
                v = v * 10 + num
                num += 1
            if(v < n) :
                if(num >= 10) :
                    v = 0
                    num = 1
                    d = 1
                    while(v < n and num <= 9) :
                        v = v * 10 + num
                        d *= 10
                        num += 1
                else :
                    l = v % (d / 10)
                    v = l * 10 + num
                    num += 1
                    
            return v, d / 10, num 
        
        v, dig, k = findSmallest(low) 
        if(v < low or v > high) :
            return []
        print(v)
        res.add(v)
        sameL(v, k, dig)
        l = list(res)
        l.sort()
        return l