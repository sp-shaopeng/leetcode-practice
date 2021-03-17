class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        w = len(dungeon[0])
        h = len(dungeon)   
        dp = [[False for i in range(w)] for i in range(h)]
        dp[-1][-1] = min(dungeon[-1][-1],0)
        
        def find(x,y) :
            if(dp[x][y] != False) :
                return dp[x][y]
            
            else:
                a = -99999999
                b = -99999999
                if(x < h - 1) :
                    a = find(x + 1, y)
                if(y < w - 1) :
                    b = find(x, y + 1)
                if(a != -99999999 and b != -99999999) :
                    print(x,y)
                    a = a + dungeon[x][y]
                    b = b + dungeon[x][y]
                    m = max(a,b)
                    if(m >= 0) :
                        dp[x][y] = 0
                    else:
                        dp[x][y] = m
                elif(a != -99999999):
                    a = a + dungeon[x][y]
                    print("1")
                    dp[x][y] = min(a, 0)
                elif(b != -99999999) :
                    b = b + dungeon[x][y]
                    print("2")
                    dp[x][y] = min(b, 0)
                    
                return dp[x][y] 
        find(0,0) 
            
        if(dp[0][0] > 0) :
            return 1
        return dp[0][0] * -1 + 1
        
        
        