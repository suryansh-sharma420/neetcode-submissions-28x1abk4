class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #take a window which contains majority characters
        #window should have characters with min frequencies summing up to k
        #windowlen - maxfreq character <= k- that tells what to replace


        l = 0
        maxlen = 0
        hashmap = {}
        max_freq = 0
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            max_freq= max(max_freq, hashmap[s[r]])
            while (r-l+1) - max_freq > k:
                hashmap[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r-l+1)
        return maxlen