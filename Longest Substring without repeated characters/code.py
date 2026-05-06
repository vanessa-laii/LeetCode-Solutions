class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        n = len(s)
        maxLength = 0
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxLength = max(maxLength, r-l+1)   
        return maxLength


        




        