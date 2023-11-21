class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        sorted_nums = sorted(nums)

        for i in range(0, len(sorted_nums), 2):
            sum += sorted_nums[i]
        return sum