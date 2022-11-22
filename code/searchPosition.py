from ast import List


class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)
                

print(Solution.searchInsert(Solution,nums = [1,3,5,6],target = 5))
print(Solution.searchInsert(Solution,nums = [1,3,5,6], target = 2))
print(Solution.searchInsert(Solution,nums = [1,3,5,6], target = 7))