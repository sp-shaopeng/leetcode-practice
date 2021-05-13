class UndergroundSystem(object):

    def __init__(self):
        self.timeMap = {}
        self.idMap = {}
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.idMap[id] = [stationName, t]
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        s, startTime = self.idMap[id]
        time = t - startTime
        time = time * 1.0
        key = s+"-"+stationName
        if(key in self.timeMap) :
            avgTime, count = self.timeMap[key]
            newT = (avgTime * count + time) / (count + 1)
            self.timeMap[key] = [newT, count + 1]
        else :
            self.timeMap[key] = [time, 1]
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return self.timeMap[startStation+"-"+endStation][0]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)