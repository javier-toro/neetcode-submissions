class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_target = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diff_to_target.keys():
                return [diff_to_target[nums[i]], i]
            diff_to_target[diff] = i 
