class Solution:        
    def searchInsert(self, nums: List[int], target: int, mid = 0) -> int:
        # mid = len(nums)//2
        # if nums[mid]>target:
        #     if nums[mid-1]<target:
        #         return mid
        #     elif nums[mid-1]==target:
        #         return mid-1
        #     mid = mid//2
        #     searchInsert(numsa,target,mid)
        # elif nums[mid]<target:
        #     if nums[mid+1]>target:
        #         return (mid+1)
        #     mid = mid + (mid//2)
        #     searchInsert(nums,target,mid)
        # elif nums[mid]==target:
        #     return mid
        if target in nums:
            return nums.index(target)
        else:
            if nums[-1]<target:
                return (len(nums))
            if nums[0]>target:
                return (0)
            
            for i in range(len(nums)-1):
                if nums[i]<target and nums[i+1]>target:
                    return (i+1)
                