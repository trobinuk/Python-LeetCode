# My solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_i,i in enumerate(nums):
            for idx_j,j in enumerate(nums):
                if idx_i != idx_j:
                    if i+j == target:
                        return [idx_i,idx_j] 

# Better Solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            nums[i] = None #If this is not there then same value will be returned
            if remaining in nums:
                return [i, nums.index(remaining)]
# Exercise
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, value in enumerate(nums):
            print(nums[i])
            remaining = target - nums[i]
            nums[i] = None
            print(remaining)
            print(nums)
            if remaining in nums:
                return [i, nums.index(remaining)]

solution = Solution()
solution.twoSum([7,2,13,11],9)


                    