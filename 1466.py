class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        tracker = [-1] * n
        total = 0
        leftover = []
        for ls in connections:
            if(ls[1] == 0):
                tracker[ls[0]] = 1
            
            elif(ls[0] == 0) :
                tracker[ls[1]] = 0
            else:
                leftover.append(ls)
        
        for i in range(n):
            if(tracker[i] == 0):
                tracker[i] = 1
                total += 1
        while(len(leftover) > 0):
            left = []
            for ls in leftover:
                if(tracker[ls[1]] == 1):
                    tracker[ls[0]] = 1
                elif(tracker[ls[0]] == 1):
                    tracker[ls[1]] = 1
                    total += 1
                else:
                    left.append(ls)
            leftover = left
        
        return total
            
            
            
            
            
            
            
        
        