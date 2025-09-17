class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #soln1
        # nums = nums[len(nums)-k::] + nums[0:(len(nums)-k)]
        # return(nums)
        #soln2
        for i in range(k):
            ele = nums[-1]
            nums.pop(-1)
            nums.insert(0,ele)