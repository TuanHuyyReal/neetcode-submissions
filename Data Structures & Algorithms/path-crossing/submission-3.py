class Solution:
    def isPathCrossing(self, path: str) -> bool:
        stepped = {(0,0)}
        x = 0
        y = 0
        for d in path:
            if d == "N": y+=1
            if d == "S": y-=1
            if d == "E": x+=1
            if d == "W": x-=1
            if (x,y) in stepped: return True
            stepped.add((x,y))
        
        return False