class Solution:

    def encode(self, strs: List[str]) -> str:
        # numbers, special chars, lower and upper case
        # total string length (reasonable)
        # time constraints (O(n))
        result = ""
        for word in strs:
            length = str(len(word))
            result += length + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        #5#Hello5#World3##!0
        result = []
        i = 0
        while i<len(s):
            j = i
            # i is the start of the length
            # j until the #
            while s[j] != "#":
                j+=1
            length = int(s[i:j])

            i = j+1
            # i is the start of the word
            word = s[i:i+length]
            i += length
            result.append(word)
        return result 


