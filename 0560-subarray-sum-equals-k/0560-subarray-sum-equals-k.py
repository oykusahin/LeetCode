class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        seen = {0: 1}
        for n in nums:
            prefixSum += n
            count += seen.get(prefixSum - k, 0)   # every valid start, at once
            seen[prefixSum] = seen.get(prefixSum, 0) + 1
        print(seen)
        return count