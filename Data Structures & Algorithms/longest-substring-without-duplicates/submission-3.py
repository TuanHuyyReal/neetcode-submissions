class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ''
        res = 0
        for ch in s:
            if ch not in window:
                window += ch
                res = max(len(window), res)
            else:
                while ch in window:
                    window = window[1:len(window)]
                window += ch
        return res