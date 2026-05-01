# my initial try
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # are the strings all lowercase
        # how big is the input size
        result = collections.defaultdict(list)

        # build the hashmap
        for word in strs:
            sMap = {}
            for value in word:
                sMap[value] = sMap.get(value, 0) + 1
            
            key = frozenset(sMap.items())
            result[key].append(word)  

            # returnt eh values in the dictionary as a list
        
        return list(result.values())


# more optimized, turning it into a frequency array
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # are the strings all lowercase
        # how big is the input size
        result = collections.defaultdict(list)

        # build the hashmap
        for word in strs:
            sMap = [0] * 26
            for letter in word:
                sMap[ord(letter) - ord('a')] += 1 
            
            result[tuple(sMap)].append(word)  

            # returnt eh values in the dictionary as a list
        
        return list(result.values())
        