class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        domain = [[1 for _ in range(n)] for __ in range(n)]

        ans = []
        def find(domain, row) :
            # print("row is ", row, " and domain, ", domain)
            if(row == n - 1):
                checkComplete = True
                for i in range(n):
                    if(sum(domain[i]) != 1) :
                        checkComplete = False
                        break
                if(checkComplete):
                    o = []
                    for i in range(n):
                        s = ""
                        for j in range(n):
                            if (domain[i][j] == 0):
                                s += "."
                            else:
                                s += "Q"
                        o.append(s)
                    # print("ooooo", o)
                    ans.append(o)
                    return
            
            for i in range(n) :
                if(sum(domain[i]) == 0) :
                    return

            for i in range(n):
                # print(row, i)
                # print(domain)
                if(domain[row][i] == 1) :
                    r = []
                    for l in range(len(domain)):
                        rr = []
                        for m in domain[l]:
                            rr.append(m)
                        r.append(rr)
                    for k in range(n) :
                        r[row][k] = 0
                        r[k][i] = 0

                    r1 = row
                    c1 = i
                    while(r1 < n and c1 < n):
                        r[r1][c1] = 0
                        r1 += 1
                        c1 += 1
                    
                    r1 = row
                    c1 = i
                    while(r1 >= 0 and c1 >= 0):
                        r[r1][c1] = 0
                        r1 -= 1
                        c1 -= 1
                    

                    
                    r2 = row
                    c2 = i
                    while(c2 < n and r2 >= 0):
                        r[r2][c2] = 0
                        r2 -= 1
                        c2 += 1
                    
                    r3 = row
                    c3 = i
                    while(c3>= 0 and r3 < n ):
                        r[r3][c3]= 0
                        r3 += 1
                        c3 -= 1
                
                
                    r[row][i] = 1
                    
                    find(r, row + 1)
        find(domain, 0)
        return ans