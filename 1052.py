class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        l = len(customers)
    
        head = 0
        tail = 0
        change = -99999
        optimal = 0
        actual = 0
        
        for i in range(l) :
            if(grumpy[i] == 1):
                grumpy[i] = 0
            else:
                grumpy[i] = 1
        
        for i in range(X):
            optimal += customers[i]
            actual += customers[i] * grumpy[i]
            tail = i
        
        change = optimal - actual
        for i in range(l - X ):
            actual = actual - customers[i] * grumpy[i] + customers[i + X ] * grumpy[i + X ] 
            optimal = optimal - customers[i] + customers[i+X ]
            if(optimal - actual >change):
                change = optimal - actual
                head = i + 1
                tail = i + X 
        for i in range(head, tail + 1) :
            grumpy[i] = 1
        ans = 0
        for i in range(l):
            ans += grumpy[i] * customers[i]
        return ans
            