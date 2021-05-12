class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        curr = 0
        for i in range(len(intervals)) :
            if(curr > intervals[i][0]):
                return False
            else:
                curr = intervals[i][1]
        
        return True
        