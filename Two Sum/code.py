class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # can i assume each element will onyl be used once?
        # will there be multiple valid solutions?

        compliments = {}
        for num in range(len(nums)):
            compliment = target - nums[num]
            if compliment in compliments:
                return [compliments[compliment], num] 
            
            else:
                compliments[nums[num]] = num 

    
        