class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, v = 1, 1

        prev = nums[0]
        while (i<len(nums)):
            prev = nums[i-1]
            if (nums[i] ==  prev):
                v+=1
                if v > 2:
                    nums.remove(nums[i])
                    continue
                else:
                    i+=1
            else:
                v = 1
                i += 1