class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ctr = {}
        for i in range(len(nums)):
            if nums[i] not in ctr:
                ctr[nums[i]]=1
            else:
                ctr[nums[i]]+=1
        for k,v in ctr.items():
            if v==1:
                return k
            
        # return