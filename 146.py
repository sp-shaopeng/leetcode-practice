class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.queue = []
        self.limit = capacity
        
        self.mapping = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i in range(len(self.queue) + 1) :
            if(i == len(self.queue)) :
                return -1
            if(self.queue[i] == key):
                break
        
        del self.queue[i]
        self.queue.append(key)
        return self.mapping[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        
        if(key in self.mapping) :
            self.mapping[key] = value
            for i in range(len(self.queue)) :
                if(self.queue[i] == key) :
                    break
            del self.queue[i]
            self.queue.append(key)
            return
        
        
        if(len(self.queue) < self.limit) :
            self.queue.append(key)
            self.mapping[key] = value
        else :
            self.mapping[key] = value
            self.queue.append(key)
            del self.mapping[self.queue[0]]
            del self.queue[0]
            
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)