class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = {}
        for i, n in enumerate(nums):
            if n in dup.keys():
                if i - dup[n] <= k:
                    return True
            dup[n]= i
        return False