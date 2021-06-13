class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        
        if(m * k > len(bloomDay)) :
            return -1
        
        right = max(bloomDay)
        left = 1
        
        while(left < right) :
            mid = (right + left) / 2
            count = 0
            consecutive = 0
            for i in range(len(bloomDay)) :
                if(bloomDay[i] <= mid) :
                    consecutive += 1
                    if(consecutive == k) :
                        count += 1
                        consecutive = 0
                else :
                    consecutive = 0
            if(count >= m):
                right = mid
            else:
                left = mid + 1
        return int(right)
        
        