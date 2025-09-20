class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        base = [1]
        for i in range(rowIndex):
            padded = [0] + base + [0]
            t = []
            for i in range(len(padded)-1):
                t.append(padded[i]+padded[i+1])
                base = t
        return base
