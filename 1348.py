class TweetCounts(object):

    def __init__(self):
        self.map = {}

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        if(tweetName in self.map) :
            self.map[tweetName].append(time)
        else:
            self.map[tweetName] = [time]
        

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        if(freq == "minute") :
            freq = 60
        elif (freq == "hour") :
            freq = 3600
        else :
            freq = 86400
        
        
        l = int(math.ceil((endTime - startTime) / freq))
        print(l)
        count = [0 for i in range(l + 1)]
        time = startTime
        ls = self.map[tweetName]
        ls.sort()
        
        for i in range(len(ls)) :
            if(ls[i] > endTime) :
                return count
            elif(ls[i] >= startTime) :
                pos = (ls[i] - startTime) / freq
                count[pos] = count[pos] + 1
            
        return count
        
        
        
        
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)