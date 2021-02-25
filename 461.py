class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # xor:
        # 1. 0 1: 1
        # 2. 1 0: 1
        # 3. 1 1: 0
        # 4. 0 0: 0
        return bin(x ^ y).count("1")