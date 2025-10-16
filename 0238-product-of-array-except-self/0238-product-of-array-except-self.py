class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suf = [1] * len(nums)
        v = 1
        for i in range(1,len(nums)):
            pref.append(v*nums[i-1])
            v = pref[i]
        vv = 1
        for j in range(len(nums)-2, -1, -1):
            vv *= nums[j+1]
            suf[j] = vv
        for i in range(len(nums)):
            nums[i] = pref[i] * suf[i]
        return nums