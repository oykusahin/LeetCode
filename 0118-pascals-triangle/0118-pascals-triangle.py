class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        p_rows = self.generate(numRows - 1)
        p_row =  [0] + p_rows[-1] + [0]
        t = []

        for i in range(len(p_row)-1):
            t.append(p_row[i]+p_row[i+1])

        p_rows.append(t)
        return p_rows