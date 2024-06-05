class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1)<len(nums2):
            a = nums1
            b = nums2
        else:
            a = nums2
            b = nums1
            
        for i in a:
            if i in b:
                res.append(i)
                b.remove(i)
        return res
        