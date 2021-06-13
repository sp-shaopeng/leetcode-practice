class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        mapper = {}
        
        if(len(arr) != len(target)) :
            return False
        
        for i in range(len(target)) :
            mapper[target[i]] = mapper.get(target[i], 0) + 1
        
        for i in range(len(target)) :
            if(arr[i] not in mapper or mapper[arr[i]] == 0) :
                return False
            else:
                mapper[arr[i]] = mapper[arr[i]] - 1
        return True