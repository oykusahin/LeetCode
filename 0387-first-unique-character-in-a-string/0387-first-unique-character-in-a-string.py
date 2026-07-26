class Solution:
    def firstUniqChar(self, s: str) -> int:
        unq = {}
        for s_elem in s:
            unq[s_elem] = unq.get(s_elem, 0) + 1
        for i, s_elem in enumerate(s):
            if unq[s_elem] == 1:
                return i
        return -1