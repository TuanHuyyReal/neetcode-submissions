class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for p in details:
            if int(p[11:13]) > 60: c+= 1
        return c