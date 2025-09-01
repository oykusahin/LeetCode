import heapq
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p: int, t: int) -> float:
            return (p+1)/(t+1)-p/t
        heap = []
        for p,t in classes:
            heapq.heappush(heap, (-gain(p,t),p,t))
        for _ in range(extraStudents):
            neg_g, p, t = heapq.heappop(heap)
            p,t = p+1, t+1
            heapq.heappush(heap, (-gain(p,t),p,t))
        total = 0.0
        while heap:
            _,p,t=heapq.heappop(heap)
            total += p/t
        return total/len(classes)