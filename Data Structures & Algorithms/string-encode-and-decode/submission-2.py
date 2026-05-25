class Solution:

    def encode(self, strs: List[str]) -> str:
        #record length
        #keep a seperator
        #append together
        #format -- length#string
        if not strs:
            return ""
        
        res = ""
        
        for s in strs:
            res += str(len(s)) + "#" + s

        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
    
        
        i = 0 #ptr 1 - traverse length till # to get length value
        while i < len(s):
            j = i #ptr2 - traverse after # to get the length of the word
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #j stops at #, length is till before #, exclusive
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
        
