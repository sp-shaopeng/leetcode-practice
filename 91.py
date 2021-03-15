class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        tracker = [-1 for i in range(l)]
        
        if(int(s[0]) == 0):
            return 0
        else:
            tracker[0] = 1
            
        
        def find(pos):
            if(tracker[pos] != -1):
                return tracker[pos]
            
            v = int(s[pos])
            lv = -1
            if(pos > 0):
                lv = int(s[pos-1:pos + 1])
            
            if(v == 0 and (lv > 26 or lv == 0)):
                tracker[pos] = 0 
            elif(v == 0):

                if(pos > 1) :
                    tracker[pos] = find(pos - 2)
                else:
                    tracker[pos] = 1
                
            elif(lv == v) :
                if(pos >= 1) :
                    tracker[pos] = find(pos - 1)
            elif(lv > 26):
                tracker[pos] = find(pos - 1) 
            else:
                if(pos > 1):
                    tracker[pos] = find(pos - 1) + find(pos - 2)
                else:
                    tracker[pos] = 1 + find(pos - 1)
            return tracker[pos]
        
        find(l - 1)
        if(tracker.count(0) > 0):
            return 0
        else:
            return tracker[l-1]
        
        
        
        
        