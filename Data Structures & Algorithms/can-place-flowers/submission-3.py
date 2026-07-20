class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = flowerbed
        # Copying the bed to avoid modifying while checking constraints
        orig = list(flowerbed)
        for i in range(len(flowerbed)):
            if orig[i] == 1:
                if i - 1 >= 0: f[i-1] = -1
                if i + 1 < len(flowerbed): f[i+1] = -1

        c = 0
        for i in range(len(f)):
            if f[i] == 0:
                c += 1
                f[i] = -1
                if i + 1 < len(f): f[i+1] = -1
        
        return c >= n