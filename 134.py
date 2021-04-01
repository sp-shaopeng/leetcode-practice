class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        d = []
        l = len(gas)
        for i in range(l):
            d.append(gas[i] - cost[i])
   
        
        if(sum(d) < 0) :
            return -1
        # print(d)
        
        pointer = 0
        s = 0
        n = 0
        for i in range(l):
            if(s + d[i] < 0) :
                pointer = i + 1
                n += s + d[i]
                s = 0
            else :
                s = s + d[i]
        
        if(pointer <= l - 1) :
            return pointer
        
        return -1
        
        
        
        
        