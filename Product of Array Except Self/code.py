class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix array
        n = len(nums)
        prefix = [1]*n
        running = 1
        for i in range(1, n):
            print(nums[i-1])
            running *= nums[i-1]
            prefix[i] = running
        
        print (prefix)


        #suffix array
        suffix = [1]*n
        running = 1
        for j in range(n-2, -1, -1):
            running *= nums[j+1]
            suffix[j] = running
        print(suffix)

        #join them
        return [x*y for x, y in zip(prefix, suffix)]


### optimized for space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix array
        n = len(nums)
        result = [1]*n
        running = 1
        for i in range(1, n):
            running *= nums[i-1]
            result[i] *= running
        


        #suffix array
        running = 1
        for j in range(n-2, -1, -1):
            running *= nums[j+1]
            result[j] *= running

        #join them
        return result
        