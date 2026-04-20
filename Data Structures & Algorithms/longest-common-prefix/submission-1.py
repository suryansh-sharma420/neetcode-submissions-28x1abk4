class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # horizontal scanning: prefix, i loop to track word, while j loop to track char
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(strs[i]), len(prefix)):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix



        
        

        # #vertical scan optimal
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return s[:i]
        
        # return strs[0]