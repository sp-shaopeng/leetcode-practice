class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dis = {}
        for i in points :
            x, y = i
            d = x * x + y * y
            if(d in dis) :
                dis[d].append(i)
            else :
                dis[d] = [i]
            
        keys = dis.keys()
        keys.sort()
        ans = []
        for i in keys :
            if(k == 0) :
                return ans
            ans += dis[i]
            k -= len(dis[i])
        return ans