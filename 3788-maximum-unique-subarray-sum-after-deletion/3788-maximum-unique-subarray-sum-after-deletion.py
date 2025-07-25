class Solution:
    def maxSum(self, nums: List[int]) -> int:
        set_nums = set(nums)
        if max(nums)<0:
            return max(nums)
        else:
            r = 0
            for n in set_nums:
                if n > 0:
                    r += n
            return r
        