class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        for i, n in enumerate(nums):
            if i > k:
                window.remove(nums[i - k - 1])
            if n in window:
                return True
            window.add(n)
        return False