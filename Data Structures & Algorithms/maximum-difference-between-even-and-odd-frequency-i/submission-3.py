class Solution:
    def maxDifference(self, s: str) -> int:
        k = {}
        for ch in s:
            if ch not in k: k[ch] = 1
            else: k[ch] += 1
        a_1 = 0 # so le
        a_2 = len(s) # so chan

        for ch in k:
            if k[ch]%2 == 0: a_2 = min(a_2,k[ch])
            else: a_1 = max(a_1,k[ch])
        return a_1 - a_2