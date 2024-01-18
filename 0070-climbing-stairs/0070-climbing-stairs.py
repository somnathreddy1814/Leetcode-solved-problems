class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        first = 1
        second = 2
        ans=0
        for i in range(2,n):
            ans = first + second
            first = second
            second = ans
        return ans
        