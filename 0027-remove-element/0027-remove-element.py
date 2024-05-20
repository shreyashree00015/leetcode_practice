class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k=0
        i=0
        while i<n:
            if nums[i]==val:
                nums.pop(i)
                n-=1
            else:
                k+=1
                i+=1
        return k