class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums) 
        dp = {}
        def recur(index, end):
            if index >= end:
                return 0
            if (index, end) in dp:
                return dp[(index, end)]

            take = recur(index + 2, end) + nums[index]
            skip = recur(index + 1, end) 
            dp[(index, end)] = max(take, skip)

            return dp[(index, end)]

        return max(recur(0, length - 1), recur(1, length))