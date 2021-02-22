class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        h = len(matrix)
        w = len(matrix[0])
        
        for i in range(h):
            for j in range(w):
                if(matrix[i][j] == target):
                    return True
                if(matrix[i][j] > target):
                    return False
        return False
        