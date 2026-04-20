class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        
        
        for i in range(len(t)): 
            s_map[s[i]] = s_map.get(s[i], 0) + 1 # this stores character and frequency
            if t[i] in t_map:
                t_map[t[i]] += 1
            else:
                t_map[t[i]] = 1
        
        if t_map == s_map:
            return True
        
        return False