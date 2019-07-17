class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        flag_map = {}
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if (
                    val == 0
                    and "".join([str(nums[i]), str(nums[left]), str(nums[right])])
                    not in flag_map
                ):
                    result.append([nums[i], nums[left], nums[right]])
                    flag_map[
                        "".join([str(nums[i]), str(nums[left]), str(nums[right])])
                    ] = True
                    left += 1
                    right -= 1
                elif val < 0:
                    left += 1
                else:
                    right -= 1
        return result
