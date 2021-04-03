class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        
        def find(arr, m):
            if(arr!= None and len(arr) == k) :
                ans.append(arr)
            elif(m<=n):
                a = []
                b = []
                if(arr != None):
                    a = arr[:]
                    b = arr[:]
                a.append(m)
                find(a,m + 1)
                find(b,m + 1)
                
        find([], 1)
        return ans