class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 'a'
        i = 1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                nums.remove(nums[i])
            else:
                i+=1
        return len(nums)