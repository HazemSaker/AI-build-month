class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sums = {}

        for i in range(len(nums)):
            if target - nums[i] in sums:
                return [i, sums[target - nums[i]]]
            else:
                sums[target - nums[i]] = i
                