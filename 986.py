class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        
        first = 0
        second = 0
        
        l = len(firstList)
        ll = len(secondList)
        
        ans = []
        
        
        while(first < l and second < ll) :
            
            if(secondList[second][0] > firstList[first][1]) :
                first += 1
                continue
            elif( firstList[first][0] > secondList[second][1]  ) :
                second += 1
                continue
            if(firstList[first][0] <= secondList[second][0]) :
                if(secondList[second][1] > firstList[first][1]) :
                    ans.append([secondList[second][0], firstList[first][1]])
                    first += 1
                else:
                    ans.append(secondList[second])
                    second += 1
            else:
                if( firstList[first][1] > secondList[second][1]) :
                    ans.append([firstList[first][0], secondList[second][1]])
                    second += 1
                    continue
                else:
                    ans.append(firstList[first])
                    first += 1
                    
        return ans
            
            
            
            