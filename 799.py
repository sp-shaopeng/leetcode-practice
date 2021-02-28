class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        res = [0 for i in range(query_row + 2)]
        res[0] = poured
        for i in range(1, query_row + 1):
            for j in range(i, -1 ,-1):
                res[j] = max(res[j] - 1, 0) / 2.0 + max(res[j - 1] - 1, 0) / 2.0

        return min(res[query_glass], 1)