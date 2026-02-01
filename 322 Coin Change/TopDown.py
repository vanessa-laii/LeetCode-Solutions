class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # backtracking
        # initialize global variables
        # recursive function
        DP = {}

        def recur(amount):

            best = float("inf")

            # base case
            if amount == 0:
                return 0
            
            if amount in DP:
                return DP[amount]
            
            
            for coin in coins:
                if amount - coin < 0:
                    continue
                res =  recur(amount - coin)
                if  res != -1:
                    best = min(best, 1 + res)
                
            
            DP[amount] = best if best != float("inf") else -1
            
            return DP[amount]
        
        return recur(amount)

            



            
