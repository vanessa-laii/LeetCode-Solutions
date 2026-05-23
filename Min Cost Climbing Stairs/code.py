class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = {}
        #returns cost
        def recur(index):
            if index in dp:
                return dp[index]
            # because there will be no more cost past index
            if index >= length:
                return 0 

            one = recur(index + 1) + cost[index]
            two = recur(index + 2) + cost[index]
            dp[index] = min(one, two)
            return dp[index]
        
        return min(recur(0), recur(1))

        