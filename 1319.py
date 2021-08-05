class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        edge = len(connections)
        if(edge < n - 1) :
            return -1
        
        removable = []
        connected = []
        placement = {}
        
        def shift(head, tail) :
            for n in connected[tail] :
                connected[head].append(n)
                placement[n] = head
            connected[tail] = []
            
            
        for i in range(edge) :
            head, tail = connections[i]
            h = placement.get(head, -1)
            t = placement.get(tail, -1)
            
            if(h == t and t != -1) :
                removable.append(connections[i])
            
            elif(h != -1 and t == -1) :
                connected[h].append(tail)
                placement[tail] = h
            elif(h == -1 and t != -1) :
                connected[t].append(head)
                placement[head] = t
            elif(h == -1 and t == -1) :
                connected.append([])
                connected[-1].append(head)
                connected[-1].append(tail)
                placement[head] = len(connected) - 1
                placement[tail] = len(connected) - 1    
            else :
                shift(h, t)
        
        

        c = sum([1 for i in connected if len(i) > 0])
        lone = 0
        for i in range(n) :
            if (i not in placement) :
                lone += 1
        return c + lone - 1
        
        
        