class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        listS = {}
        listT = {}

        for i in range(len(s)):
            listS[s[i]] = listS.get(s[i], 0) + 1 
            listT[t[i]] = listT.get(t[i], 0) + 1 
        
        return listS == listT