class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        n = len(isConnected)
        visited = set()
        count = 0
        for k in range(n) :
            if(k not in visited) :
                count += 1
                queue = [k]
                newQ = []
                while(queue) :
                    while(queue) :
                        node = queue.pop()
                        adj = isConnected[node]

                        for i in range(n) :
                            if(i != node and (adj[i] == 1 and i not in visited)) :
                                newQ.append(i)
                                visited.add(i)

                    queue = newQ

        
        return count
        
        