class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        DP = {}
        def recur(index):
            # base case
            if index >= length:
                ## DP need an actual return value
                return 0

            if index in DP:
                return DP[index]
            
            # call the recur with take or skip
            take = recur(index + 2) + nums[index]

            skip = recur(index + 1)
            best = max(take, skip)
            DP[index] = best

            return best
        
        return recur(0)