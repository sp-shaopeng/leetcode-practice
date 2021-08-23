class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d = {}
        for i in nums :
            d[i] = d.get(i, 0) + 1
        
        k = list(d)
        k.sort(reverse = True)
        
        c = 0
        s = 0
        for i in range(len(k) - 1) :
            s += d[k[i]]
            c += s
        return c