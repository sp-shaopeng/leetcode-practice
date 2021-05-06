class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[] for i in range(numRows)]
        res[0].append(1)
        
        for i in range(1, numRows):
            for j in range(i + 1) :
                if(j == 0 or j == i ) :
                    res[i].append(1)
                else:
                    v = res[i-1][j - 1] + res[i-1][j]
                    res[i].append(v)
        return res
        
        