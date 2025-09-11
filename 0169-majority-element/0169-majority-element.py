class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pickEle, countOfEle = None, 0
        for num in nums:
            if countOfEle == 0:
                pickEle = num
            countOfEle += (1 if num == pickEle else -1)
        return pickEle
        