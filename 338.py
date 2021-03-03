class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        
        ans = []
        for i in range(num + 1):
            v = str(bin(i))
            ans.append(v.count("1"))
        
        return ans