class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()
        
        if(len(s) == 0):
            return 0
        
        p = s[0]
        s = s[1:]
        
        size = len(s)
        i = 0
        tail = ""
        while(i < size):
            if(s[i].isdecimal()):
                tail = tail + s[i]
                i = i + 1
            else :
                break;
        

            
        
        if(p.isdecimal()):
            print("2")
            tail = p + tail
            ints = int(tail)
            if(ints <= 2**31 -1):
                return ints
            else:
                return 2**31 -1
        elif(p == "+") :
            if(len(tail) == 0):
                return 0
            ints = int(tail)
            if(ints <= 2**31 -1):
                return ints
            else:
                return 2**31 -1
        elif(p == "-") :
            print("3")
            if(len(tail) == 0):
                return 0
            ints = - int(tail)
            if(ints > -2**31):
                return ints
            else:
                return -2**31
        else :
            return 0
            
        
        
        