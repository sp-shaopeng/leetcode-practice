class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        order = sorted(intervals, key = lambda x: x[0])
        
        ans = []
        curr = order[0]
        for i in range(1 , len(order)):
            if(order[i][0] > curr[1]) :
                ans.append(curr)
                curr = order[i]
            else :
                if(curr[1] < order[i][1]) :
                    curr[1] = order[i][1]
        ans.append(curr)
        return ans
            
            
            
            