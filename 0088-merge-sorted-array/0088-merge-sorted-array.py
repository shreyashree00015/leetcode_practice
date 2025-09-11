class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        pt1 = 0
        pt2 = 0
        while (pt2<n):
            if (pt1==len(nums1)):
                nums1+=nums2[pt2:]
                break
            if (nums1[pt1]<nums2[pt2]):
                pt1+=1
            elif (nums1[pt1]>=nums2[pt2]):
                nums1.insert(pt1,nums2[pt2])
                pt2+=1
                pt1+=1