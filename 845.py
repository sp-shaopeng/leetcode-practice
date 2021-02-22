class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """


            
        
        increase = 0
        decrease = 0
        ans = 0
        
        #append last one to make it ==
        arr.append(arr[len(arr) - 1])
        
        for i in range(len(arr) - 1):
            if(arr[i] == arr[i+1]) :
                # it is increasing
                if(decrease == 0) :
                    increase = 0
                    decrease = 0
                else :
                    decrease = decrease + 1
                    current = increase + decrease
                    if(current > ans):
                        print("here", i,arr[i], current)
                        ans = current
                    increase = 0
                    decrease = 0
                        
                        
            elif(arr[i] < arr[i+1]) :
                if(decrease == 0):
                    increase = increase + 1
                else:
                    decrease = decrease + 1
                    current = increase + decrease
                    if(current > ans):
                        print(i,arr[i], current)
                        ans = current
                    increase = 1
                    decrease = 0
            else:
                if(increase > 0) :
                    decrease = decrease + 1
                else:
                    increase = 0
                    decrease = 0
                    
                

        return ans
                
        
        