class Solution:
    def canJump(self, nums: List[int]) -> bool:
        globalMax = 0
        for i in range(len(nums)):
            if globalMax < i:
                return False
            if globalMax >= len(nums)-1:
                return True
            current = i + nums[i]
            globalMax = max(globalMax, current)
        
        return True
        