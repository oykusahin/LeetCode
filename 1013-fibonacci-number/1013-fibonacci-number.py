class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b, c = 0, 1, 0
 
        for i in range(n):
            if i != 0:
                c = a + b
                a = b
                b = c
        return c