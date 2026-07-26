class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = {}
        for i, n in enumerate(nums):
            if n not in dup.keys():
                dup[n]= i
            else:
                if i - dup[n] <= k:
                    return True
                else:
                    dup[n] = i
        return False