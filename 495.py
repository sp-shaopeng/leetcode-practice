class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
  
        l = len(timeSeries)
        if(l == 0) :
            return 0
        total = 0
        end = timeSeries[0] + duration
        for i in range(1,l) :
            if(timeSeries[i] >= end) :
                total += duration
      
            else :
                total += timeSeries[i] -  timeSeries[i - 1]
            
            end = timeSeries[i] + duration
            
        return total + duration
        