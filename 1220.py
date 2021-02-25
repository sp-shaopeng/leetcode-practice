class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        tracker = [[-1 for i in range(5)] for j in range(n)]
        for i in range(5):
            tracker[0][i] = 1
        def find(letter,c):
            if(tracker[c][letter] != -1):
                return tracker[c][letter]
            
            if(letter == 0):
                tracker[c][letter] = find(1, c - 1)
            
            if(letter == 1):
                tracker[c][letter] = find(0, c - 1) + find(2, c - 1)
                
            if(letter == 2):
                tracker[c][letter] = find(0, c - 1) + find(1, c - 1) + find(3, c - 1) + find(4, c - 1)
            
            if(letter == 3):
                tracker[c][letter] = find(2, c - 1) + find(4, c - 1)
            
            if(letter == 4):
                tracker[c][letter] = find(0, c - 1)
                
            return tracker[c][letter]
            
        find(0,n -1)
        find(1,n -1)
        find(2,n -1)
        find(3,n -1)
        find(4,n -1)
            
        return sum(tracker[n - 1]) % 1000000007