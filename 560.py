class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        arr = [i for i in nums]
        
        store = {}
        store[arr[0]] = [0]
        for i in range(1, len(arr)) :
            arr[i] = arr[i - 1] + arr[i]
            if(arr[i] in store) :
                store[arr[i]].append(i)
            else:
                store[arr[i]] = [i]
        count = 0
        for i in range(len(arr)) :
            diff = arr[i] - k
            v = store.get(diff, [])
            if(len(v) > 0) :
                count += len([j for j in v if j < i])
            if(diff == 0) :
                count += 1
        return count
        
        
        