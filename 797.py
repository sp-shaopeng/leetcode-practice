class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        n = len(graph) - 1
        res = []
        
        def find(node, visited, path):
            visited.add(node)
            path.append(node)
            
            if(node == n) :
                res.append(path)    
                return
            for i in graph[node] :
                if(i in visited) :
                    continue
                v = visited.copy()
                p = path[:]
                find(i, v, p)
        find(0, set(), [])
        return res