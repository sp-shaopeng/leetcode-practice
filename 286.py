class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        
        visited = []
        h = len(rooms)
        w = len(rooms[0])
        print(h, w)
        Q = []
        newQ = []
        dp = [[0 for i in range(w)] for j in range(h)]
        
        for i in range(h) :
            for j in range(w) :
                if(rooms[i][j] == 0) :
                    Q.append([i,j])
                    dp[i][j] = 1
                if(rooms[i][j] == -1) :
                    dp[i][j] = 1


        def AddToQueue(pos) :
            if(pos[0] < 0 or pos[1] < 0 or pos[0] >= h or pos[1] >= w) :
                return 
            elif(dp[pos[0]][pos[1]] != 1) :
                newQ.append(pos)
                dp[pos[0]][pos[1]] = 1

        count = 0
        while(Q) :
           
            while(Q) :
                pos = Q.pop()
                
                rooms[pos[0]][pos[1]] = count
                AddToQueue([pos[0] - 1, pos[1]])
                
                AddToQueue([pos[0] + 1, pos[1]])

                AddToQueue([pos[0], pos[1] - 1])

                AddToQueue([pos[0], pos[1] + 1])
                
            count += 1
            Q = newQ
            newQ = []
                

            
        
        
        
        