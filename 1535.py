class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        record = {}
        for i in arr :
            record[i] = 0
        
        largest = max(arr)
        
        while(True):
            if(arr[0] == largest):
                return largest
            
            if(arr[0] > arr[1]) :
                # print(arr)
                pos = 1
                while(arr[0] > arr[pos]):
                    pos += 1
                
                record[arr[0]] = record.get(arr[0]) + pos - 1
                if(record[arr[0]] >= k) :
                    return arr[0]
                arr = [arr[0]] + arr[pos:] + arr[1:pos]
                # print(record)

            else:
                record[arr[1]] = record.get(arr[1]) + 1
                if(record[arr[1]] == k) :
                    return arr[1]
                arr = arr[1:] + [arr[0]]