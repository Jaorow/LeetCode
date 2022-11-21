class Solution(object):
    def twoSum(self, nums, target):
        count = 0
        i_index = 0
        j_index = 1
        for i in (nums):
            for j in nums[count+1:]:
                if i+j == target:
                    return [i_index,j_index]
                j_index+=1
            i_index += 1
            j_index = i_index + 1
            count += 1




# print(Solution.twoSum(Solution,[3,2,4], target = 6))
print(Solution.twoSum(Solution,[3,2,4], target = 6))
# print(Solution.twoSum(Solution,[3,3], target = 6))

        