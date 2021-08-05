class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        r = {}
        res = [0]
        
        for i in range(len(manager)) :
            if(manager[i] != -1) :
                temp = r.get(manager[i], [])
                if(temp) :
                    r[manager[i]].append(i)
                else :
                    r[manager[i]] = [i]
        
        def find(ids, t) :
            toInform = r.get(ids, [])
            if(toInform) :
                for i in toInform :
                    find(i, t + informTime[ids])
            else:
                res[0] = max(res[0], t)
        
        find(headID,0)
        return res[0]