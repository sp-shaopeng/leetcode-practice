class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        l = len(arr)
        e = set()
        e.add(start)
        q = [start]
        
        while(q):
            pos = q.pop()
            if(arr[pos] == 0)  :
                return True
            forward = pos + arr[pos]
            if(forward < l and forward not in e):
                q.append(forward)
                e.add(forward)
            backward = pos - arr[pos]
            if(backward >= 0 and backward not in e):
                q.append(backward)
                e.add(backward)
        return False

        