class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        connected = []
        
        def unionSet(curr, val) :
            for i in range(len(connected)) :
                if(val in connected[i] and i != curr) :
                    connected[curr] = connected[curr].union(connected[i])
                    return i
            return -1
        for i in edges :
            x, y = i
            c = -2
            # print(connected)
            for j in range(len(connected)) :
                if(x in connected[j] and y in connected[j]) :
                    return i
                elif(x in connected[j]) :
                    connected[j].add(y)
                    c = unionSet(j, y)
                elif(y in connected[j]) :
                    connected[j].add(x)
                    c = unionSet(j, x)
            # print(i, c)
            if(c == -2) :
                newS = set()
                newS.add(x)
                newS.add(y)
                connected.append(newS)
            elif(c != -1) :
                connected.pop(c)
        
        