class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # solution 1
        
        # i, v = 1, 1
        # while (i<len(nums)):
        #     if (nums[i] ==  nums[i-1]):
        #         v+=1
        #         if v > 2:
        #             nums.remove(nums[i])
        #             continue
        #         else:
        #             i+=1
        #     else:
        #         v = 1
        #         i += 1
        
        i, v = 1, 0
        writeIndex = 1
        prevEle = nums[0]
        while (i<len(nums)):
            if (nums[i] ==  prevEle):
                v+=1
            else:
                v = 0
            if (v<=1):
                nums[writeIndex] = nums[i]
                writeIndex += 1
                prevEle = nums[i]
            i+=1
        return writeIndex