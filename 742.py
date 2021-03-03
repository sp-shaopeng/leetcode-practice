class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        tracker = [-1 for i in range(n + 1)]
        tracker[k] = 0
        store = {}
        
        for i in times:
            if (i[0] in store):
                
                store[i[0]].append([i[1],i[2]])
            else:
                store[i[0]] = [[i[1], i[2]]]
        queue = [k]
        while(len(queue) > 0):
            v = queue.pop()
            if(v in store):
                for point in store[v]:
                    if(tracker[point[0]] < 0 or tracker[v] + point[1] < tracker[point[0]]):
                        tracker[point[0]] = tracker[v] + point[1]
                        queue.append(point[0])
        m = -1
        for i in range(1, n+1):
            if(tracker[i] == -1):
                return -1
            
            m = max(m, tracker[i])
        
        return m