class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # start at our base case
        # start at amount = 0
        DP = [0] * (amount + 1)
        # ex. 5 stores the best way to make 5/ num coins, uses prev value
        for cost in range(1, amount+1):
            best = float("inf")
            for coin in coins:
                remainder = cost - coin
                if remainder < 0 or DP[remainder] == -1:
                    continue

                best = min(best, DP[remainder] + 1)
            DP[cost] = best if best != float("inf") else -1
        
        return DP[amount]

                



            



            
