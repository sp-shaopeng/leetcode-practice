class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        ptr1 = len(s1) 
        ptr2 = len(s2) 
        ptr3 = len(s3) 
        
        if(ptr1 + ptr2 != ptr3) :
            return False
            
        queue = [(0, 0)]
        visited = set()
        visited.add((0,0))
        
        while(queue) :
            x, y = queue.pop(0)
            
            if(x + y == ptr3) :
                return True
            
            if(x + 1 <= ptr1 and s1[x] == s3[x + y] and (x + 1,y) not in visited) :
                queue.append((x + 1,y))
                visited.add((x+1, y))
                
                
            if(y + 1 <= ptr2 and s2[y] == s3[x + y] and (x,y + 1) not in visited) :
                queue.append((x,y + 1))
                visited.add((x, y + 1))
            
        return False