class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_n = len(nums)

        for i in range(nums_n):
            for j in range(i+1, nums_n):   
                diff = target - nums[i]
                if nums[j] == diff:
                    return [i,j]
                

