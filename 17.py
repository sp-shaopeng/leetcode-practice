class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ls = [[],[],["a","b", "c"], ["d","e","f"], ["g","h","i"],["j","k","l"], ["m","n","o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        
        arr = [int(i) for i in digits]
        # print(arr)
        
        s = []
        for i in range(len(arr)) :
            d = arr[i]
            if(len(s) == 0) :
                s = ls[d]
            else :
                newS = []
                for m in s:
                    for n in ls[d] :
                        newS.append(m + n)
                s = newS
        return s