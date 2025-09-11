class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pt1 = 0
        pt2 = len(nums)-1
        c = 0
        while (pt1<=pt2):
            if nums[pt1]==val:
                placeholder = nums[pt1]
                nums[pt1] = nums[pt2]
                nums.pop(pt2)
                pt2-=1
                c+=1
            elif nums[pt1]!=val:
                pt1+=1
        # nums[:] = nums[:-c]
        