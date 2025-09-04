class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        ftt = abs(z-x)
        stt = abs(z-y)

        if ftt > stt:
            return 2
        elif ftt < stt:
            return 1
        else:
            return 0