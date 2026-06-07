class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums) 

        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums)
        
        
        def helper(start, stop):
            dp = [0] * (length+2)
            for i in range(start, stop, -1):
                take = nums[i] + dp[i+2]
                skip = dp[i+1]

                dp[i] = max(take, skip)
            
            return max(dp[0], dp[1])


        return max(helper(length -1, 0), helper(length - 2, -1))