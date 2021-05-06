class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [[] for i in range(rowIndex + 1)]
        res[0].append(1)
        
        for i in range(1,rowIndex + 1):
            for j in range(i + 1) :
                if(j == 0 or j == i ) :
                    res[i].append(1)
                else:
                    v = res[i-1][j - 1] + res[i-1][j]
                    res[i].append(v)
        return res[-1]
        