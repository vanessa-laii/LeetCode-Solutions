class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        globalMax = 0
        jumps, count = 0, 0
        for i in range(length):
            current = i + nums[i]
            globalMax = max(globalMax, current)
            nums[i] = globalMax
        
        while jumps < length - 1:
            jumps = nums[jumps]
            # jumps to the farthest possible index
            count += 1

        return count


        