class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        # if len(nums1)<len(nums2):
        #     a = nums1
        #     b = nums2
        # else:
        #     a = nums2
        #     b = nums1
            
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res
        