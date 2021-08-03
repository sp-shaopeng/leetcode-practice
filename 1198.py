class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        h = len(mat)
        s = 0
        index = [0 for i in range(h)]
        for i in range(h) :
            s = max(s, mat[i][0])
            
        change = True
        while(change) :
            change = False
            for i in range(h) :
                w = len(mat[i])
                while(index[i] <= w) :
                    if(index[i] == w) :
                        return -1
                    else :
                      
                        if(mat[i][index[i]] < s) :
                            index[i] += 1
                            continue
                            
                        if(mat[i][index[i]] == s) :
                            break
                            
                        if(mat[i][index[i]] > s) :
                            s = mat[i][index[i]]
                            change = True
                            break

                if(change) :
                    break
        return s