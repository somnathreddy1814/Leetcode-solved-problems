class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return math.log(n, 4) == int(math.log(n, 4)) if n > 0 else False