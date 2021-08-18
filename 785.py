class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        
        n = len(graph)
        
        dp = [-1 for i in range(n)]
        
        color = True
        
        toVisit = [i for i in range(n)]
        
        while(toVisit) :
            v = toVisit[0]
            Q = [v]
            while(Q) :
                newQ = set()
                while(Q) :
                    k = Q.pop()
                    dp[k] = color
                    toVisit.remove(k)
                    for i in graph[k] :
                        if(dp[i] == color) :
                            return False
                        if(dp[i] == -1) :
                            newQ.add(i)
                
                Q = list(newQ)
                color = not color
        return True
