class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        l = len(matrix)
        w = len(matrix[0])
        ans = [[-1 for i in range(l)] for j in range(w)]
        
        for i in range(l):
            for j in range(w):
                # print(i,j)
                ans[j][i] = matrix[i][j]
        return ans