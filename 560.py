class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = [i for i in nums]
        store = {}
        store[arr[0]] = 1
        
        count = 0
        
        if(len(arr) == 1) :
            return int(arr[0] == k) 
        
        if(arr[0] == k) :
            count += 1
        
        for i in range(1, len(arr)) :
            arr[i] = arr[i - 1] + arr[i]
            diff = arr[i] - k 
                     
            if(diff == 0) :
                count += 1
            
            if(diff in store) :
                count += store[diff]
            
            if(arr[i] in store) :
                store[arr[i]] = store[arr[i]] + 1
            else:
                store[arr[i]] = 1

                
        return count
        
        
        