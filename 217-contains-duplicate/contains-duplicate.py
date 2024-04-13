class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # This piece of code is showing time limit exceeded but can run
        '''nums.sort()
        for i in range(len(nums)):
            for j in  range(i+1 , len(nums)):
                if nums[i] == nums[j]:
                    return True                
        return False'''

        #optimised way is doing in hashset
        Set = set()
        for i in nums:
            if i in Set:
                return True
            Set.add(i)
        return False