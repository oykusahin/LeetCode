class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        toReturn = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break                                  
            if i > 0 and nums[i] == nums[i-1]:
                continue                               
            anchor = nums[i]
            nTarget = 0 - anchor                       
            left, right = i + 1, len(nums) - 1         
            while left < right:
                tSum = nums[left] + nums[right]
                if tSum == nTarget:
                    toReturn.append([anchor, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1                     
                elif tSum > nTarget:
                    right -= 1
                else:
                    left += 1
        return toReturn