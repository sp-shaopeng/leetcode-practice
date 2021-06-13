class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans = 0
        for i in range(len(digits)) :
            ans = ans * 10 + digits[i]
        ans += 1
        
        return list(str(ans))
        