class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadanes algorithm 
        currentMax, globalMax = float("-inf"), float("-inf")
        length = len(nums)
        for i in range(length):
            currentMax = max(currentMax + nums[i], nums[i])
            globalMax = max(globalMax, currentMax)
        return globalMax

        