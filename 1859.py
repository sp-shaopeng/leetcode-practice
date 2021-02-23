class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        l = len(nums)
        r = len(requests)
        w = [ 0 for i in range(l)]
        nums.sort()
        for i in range(r):
            v = requests[i]
            w[v[1]] += 1
            if(v[0] > 0):
                w[v[0] - 1] -= 1
        
        for i in range(l - 2, -1, -1):
            w[i] = w[i + 1] + w[i]
        ans = 0
        w.sort()
        for i in range(l - 1, -1, -1):
            if(w[i] == 0):
                break
            ans = ans + w[i] * nums[i]
            
        

        return ans % (1000000007)
        