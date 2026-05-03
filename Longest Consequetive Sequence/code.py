class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longestLength = 0

        for n in numSet:
            length = 1
            if n-1 not in numSet:
                while n+1 in numSet:
                    length +=1
                    n+=1
                
                longestLength = max(longestLength, length)
        
        return longestLength
        

                
        
        
            