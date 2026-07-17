class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_k = {}
        t_k = {}
        for ch in s:
            if ch not in s_k: s_k[ch] = 1
            else: s_k[ch] += 1
        for ch in t:
            if ch not in t_k: t_k[ch] = 1
            else: t_k[ch] +=1
        for key in s_k:
            if key not in t_k: return False
            
            if s_k[key] != t_k[key]: return False
        for key in t_k:
            if key not in s_k: return False
        return True