class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if(key not in self.map) :
            self.map[key] = {}
        self.map[key][timestamp] = value
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        d = self.map[key]
        if(len(d) == 0) :
            return ""
        while(timestamp >= 0) :
            if(timestamp in d) :
                return d[timestamp]
            timestamp = timestamp - 1
        return ""        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)