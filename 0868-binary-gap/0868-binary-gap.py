class Solution:
    def binaryGap(self, n: int) -> int:
        best, gap, seen_one = 0, 1, False
        while n > 0:
            if n % 2 == 1:
                if seen_one:
                    best = max(best, gap)
                seen_one = True
                gap = 1
            elif seen_one:
                gap += 1
            n //= 2
        return best
        