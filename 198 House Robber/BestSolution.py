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

        prev2 = 0
        prev1 = 0
        current = 0

        #start at length because one past is a possible value (base case)
        for n in range(length-1, -1, -1):
            take = nums[n] + prev2
            skip = prev1

            current = max(take, skip)
            prev2, prev1 = prev1, current 
        
        return prev1



        