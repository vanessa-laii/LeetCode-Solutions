class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        DP = [0] * (length + 2)

        # edge cases
        # 0 length
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])

        #start at length because one past is a possible value (base case)
        for n in range(length-1, -1, -1):
            take = nums[n] + DP[n+2]
            skip = DP[n+1]
            DP[n] = max(take, skip)
        
        return max(DP[0], DP[1])




        