class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        adj = [[] for i in range(numCourses)]
        
        visited = [0 for i in range(numCourses)]
        
        for x, y in prerequisites :
            adj[x].append(y)
            
        def dfs(node) :
            if(visited[node] == -1) :
                return False
            if(visited[node] == 1) :
                return True
            
            visited[node] = -1
            c = True
            for i in adj[node] :
                c = c and dfs(i)
                if(not c) :
                    return False
            visited[node] = 1
            return True
        
        for i in range(numCourses) :
            if not dfs(i) :
                return False
        return True
        
        
        