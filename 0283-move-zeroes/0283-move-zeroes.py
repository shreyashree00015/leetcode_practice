class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos] = nums[i]
                non_zero_pos += 1
        
        for i in range(non_zero_pos, len(nums)):
            nums[i] = 0