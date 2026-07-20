class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        k = {}
        p = {}
        for ci in range(len(s)):
            if s[ci] not in k:
                k[s[ci]] = t[ci]
            if s[ci] in k:
                if k[s[ci]] != t[ci]: return False
        for ci in range(len(t)):
            if t[ci] not in p:
                p[t[ci]] = s[ci]
            if t[ci] in p:
                if p[t[ci]] != s[ci]: return False
        return True