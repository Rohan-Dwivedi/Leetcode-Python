class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# brute force way
        '''for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []'''
# optimize way
        dict = {}
        for i, value in enumerate(nums):
            if target-value in dict:
                return dict[target-value], i
            dict[value] = i