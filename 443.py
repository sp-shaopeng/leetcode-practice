class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        pos = 0
        count = 1
        curr = chars[0]
        for i in range(1, len(chars) + 1) :
            if(i == len(chars)) :
                chars[pos] = curr
                pos += 1
                if(count > 1) :
                    v = list(str(count))
                    for i in range(len(v)) :
                        chars[pos + i] = v[i] 
                    pos += len(v)
                    
            
            elif(i < len(chars) and curr == chars[i]) :
                count += 1

            else :
                val = chars[i] 
                if(count == 1) :
                    chars[pos] = curr
                    pos += 1
                else :
                    chars[pos] = curr
                    pos += 1
                    v = list(str(count))
                    for i in range(len(v)) :
                        chars[pos + i] = v[i] 
                    pos += len(v)
                curr = val
                count = 1
        
        return pos 
        
                    
                    
                    