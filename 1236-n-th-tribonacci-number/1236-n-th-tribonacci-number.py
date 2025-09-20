class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        a,b,c,d= 0,1,1,0
        for i in range(n+1):
            if i >= 3:
                d = a + b + c
                a = b
                b = c
                c = d
                
        return d
            