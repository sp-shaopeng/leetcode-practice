class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        n = len(intervals)
        if(not n) :
            return 0
        
        room = [0]
        intervals.sort()
        
        for i in range(n) :
            for j in range(len(room) + 1) :
                if(j == len(room)) :
                    room.append(intervals[i][1])
                    break
                if(room[j] <= intervals[i][0]) :
                    room[j] = intervals[i][1]
                    break
        
        
        
        
        
        return len(room)