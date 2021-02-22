class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if(amount == 0):
            return 0
        
        tracker = [123456789 for i in range(amount + 1)]
        tracker[0] = 0
        for i in range(1, amount + 1):
            
            for j in range(len(coins)):
                
                if(i >= coins[j]):
                    tracker[i] = min(tracker[i], tracker[i - coins[j]] + 1)
        
        if (tracker[amount] == 123456789):
            return -1
        else :
            return tracker[amount]
                    
        
        
        
        