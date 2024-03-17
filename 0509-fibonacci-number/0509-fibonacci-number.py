class Solution:
    def fib(self, n: int) -> int:
        a,b=0,1
        for i in range(n):
            a,b=b,a+b

        return a
    
        # n1=0
        # n2=1
        # n3=0
        # for i in range(1,n):
        #     n3=n1+n2
        #     n1=n2
        #     n2=n3
        # return n3
            
            
            